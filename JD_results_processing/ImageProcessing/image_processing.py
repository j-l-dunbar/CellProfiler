#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  matplotlib.image as img
import skimage as ski

image = img.imread("Adt_ret_EphA5-Efna5-EphA6_JD12_s3c4.tif")
image.shape
from skimage.filters import unsharp_mask
from scipy.signal import convolve2d as conv2
from skimage import color, data, restoration
from skimage.color import rgb2gray
import psf

def make_psf():
    args = dict(dims=(4, 4), ex_wavelen=577, em_wavelen=603,
                num_aperture=0.8, refr_index=1,)
    obsvol = psf.PSF(psf.ISOTROPIC | psf.WIDEFIELD, **args) # psf.GAUSSIAN - gaussian emmision
    print(obsvol, end='')  # doctest:+ELLIPSIS
    return obsvol.data

# %%
cropped = image[6300:7300,5000:6500]
astro = rgb2gray(cropped)

point_spread = make_psf()
astro = conv2(astro, point_spread, 'same')
# Add Noise to Image
astro_noisy = astro.copy()
astro_noisy += (np.random.poisson(lam=25, size=astro.shape) - 10) / 255.

# Restore Image using Richardson-Lucy algorithm
deconvolved_RL = restoration.richardson_lucy(astro_noisy, point_spread, iterations=15)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(42, 14))
plt.gray()

for a in (ax[0], ax[1], ax[2]):
       a.axis('off')

ax[0].imshow(astro)
ax[0].set_title('Original Data')

ax[1].imshow(astro_noisy)
ax[1].set_title('Noisy data')

ax[2].imshow(deconvolved_RL, vmin=astro_noisy.min(), vmax=astro_noisy.max())
ax[2].set_title('Restoration using\nRichardson-Lucy')


fig.subplots_adjust(wspace=0.02, hspace=0.2,
                    top=0.9, bottom=0.05, left=0, right=1)
plt.show()
#%%


cropped_restore = restoration.richardson_lucy(cropped, point_spread, iterations=5)

fig, ax = plt.subplots(figsize=(14,14))
ax.imshow(cropped)
ax.set_axis_off()
plt.tight_layout()
fig.show()

plt.imshow(cropped_restore)
# %%
from math import sqrt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
image = cropped_restore
image_gray = rgb2gray(image)
blobs_log = blob_log(image_gray, min_sigma=1, max_sigma=6, num_sigma=4, threshold=.07, overlap=0.9)
# Compute radii in the 3rd column.
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)


fig, ax = plt.subplots(1, 1, figsize=(14, 14))
ax.set_title("Laplacian of Gaussian -- Blob")
ax.imshow(image)
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r, color='g', linewidth=2, fill=False)
    ax.add_patch(c)
ax.set_axis_off()
plt.tight_layout()
plt.show()

# %%