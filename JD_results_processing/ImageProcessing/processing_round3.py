# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  matplotlib.image as img
import skimage as ski


from skimage.filters import unsharp_mask
from scipy.signal import convolve2d as conv2
from skimage import color, data, restoration
from skimage.color import rgb2gray
from math import sqrt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray

file_num = 2
file_ID = {2:2.5, 3:0.25, 4:0.8}

img_name = f"Adt_ret_EphA5-Efna5-EphA6_JD12_s3c{file_num}.tif"
bright_scaling = file_ID[file_num]

# %%
def plot_result(image, background):
    fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(42,14))

    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('Original image')
    ax[0].axis('off')

    ax[2].imshow(background, cmap='gray')
    ax[2].set_title('Background')
    ax[2].axis('off')

    ax[1].imshow(image - background, cmap='gray')
    ax[1].set_title('Result')
    ax[1].axis('off')

    fig.tight_layout()



# %%
image = plt.imread(img_name)
image.shape

cropped = image[6300:7300,5000:6500]
analy_image = cropped
BandW = rgb2gray(analy_image) * bright_scaling



normalized_radius = 75/ 512

kernel = restoration.ellipsoid_kernel((50, 50), normalized_radius)
background = restoration.rolling_ball(BandW, kernel=kernel)
plot_result(BandW, background)
plt.show()


# %%
subBG = BandW - background
blobs_log = blob_log(subBG, min_sigma=3, max_sigma=11, num_sigma=8, threshold=.015, overlap=1)
# blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
blobs_filt = pd.DataFrame(blobs_log)
blobs_filt = blobs_filt[blobs_filt[2]<8]
print(f"{len(blobs_log)-len(blobs_filt.index)} rows removed")

fig, ax = plt.subplots(1, 1, figsize=(14, 14))
ax.set_title("Laplacian of Gaussian -- Blob")
# ax.imshow(analy_image)
ax.scatter(blobs_filt[0], blobs_filt[1])
plt.tight_layout()
plt.show()

# %%
