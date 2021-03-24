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

file_num = 3                                                        # channel to be analyzed
file_ID = {2:2.5, 3:0.25, 4:0.8}                                    # the image channel sets the bightness scaling factor

img_name = f"Adt_ret_EphA5-Efna5-EphA6_JD12_s3c{file_num}.tif"      # name of the file to be opened
bright_scaling = file_ID[file_num]                                  # scales the intensity of the image to work more uniformly between channels

# %%
def plot_result(image, background):                             # plots the background removal images
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
image = plt.imread(img_name)                                # opens the image specified
print(image.shape)                                          # image dimentions
# %%
cropped = image[6300:7300,5000:6500]                        # small with relebant signal to make processing easier
# cropped = image ****************************************************************************************** Breaks the code -- image too large it seems -- to many points to keep track of? ~20k points
analy_image = cropped
BandW = rgb2gray(analy_image) * bright_scaling              # makes a black and white image that is scaled by the brightness scaling factor (makes the output more consistent between image channels)



normalized_radius = 75/ 512

kernel = restoration.ellipsoid_kernel((50, 50), normalized_radius)      # Creates a kernel for determining the background
background = restoration.rolling_ball(BandW, kernel=kernel)             # makes an image representing the BG signal
plot_result(BandW, background)                                          # Plots Before, After, and the Background image
plt.show()


# %%
subBG = BandW - background                                                                      # removes the background for processing
blobs_log = blob_log(subBG, min_sigma=3, max_sigma=11, num_sigma=8, threshold=.015, overlap=1)  # Finds "blobs" in the image -- finds the puncta in this image
# blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)                                                   # Converts the sigma to a radius? -- computationaly expensive to plot all these
blobs_filt = pd.DataFrame(blobs_log)                                                            # Dataframe to make plotting easier (there should be a better equiv in numpy)
blobs_filt = blobs_filt[blobs_filt[2]<8]                                                        # removes the very large "Blobs"
print(f"{len(blobs_log)-len(blobs_filt.index)} rows removed")                                   # states what was removed

fig, ax = plt.subplots(1, 1, figsize=(14, 14))                                                  # plots the detected
ax.set_title("Laplacian of Gaussian -- Blob")
ax.imshow(analy_image)
# for _, blob in blobs_filt.iterrows():                                                         # plots the blobs as circles -- very computationally expensive compated to just the points
#     y, x, r = blob
#     c = plt.Circle((x, y), r, color='orange', linewidth=2, fill=False)
#     ax.add_patch(c)
ax.set_axis_off()
ax.scatter(blobs_filt[1], blobs_filt[0], alpha=0.5)                                             # plots transparent points on the detected "blobs"
# ax.invert_yaxis()
plt.tight_layout()
plt.show()

# %%
