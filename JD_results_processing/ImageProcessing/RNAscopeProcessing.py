# %%


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as image
import numpy as np

# img = image.imread("Adt_ret_EphA5-Efna5-EphA6_JD12_s3c3.tif")
# img.shape
# # plt.imshow(img)
# cropped = img[6300:7300,5000:6500]
# plt.imshow(cropped)
# # %%
# from math import sqrt
# from skimage import data
# from skimage.feature import blob_dog, blob_log, blob_doh
# from skimage.color import rgb2gray
# image = img
# image_gray = rgb2gray(image)
# blobs_log = blob_log(image_gray, min_sigma=1, max_sigma=6, num_sigma=4, threshold=.07, overlap=0.9)
# # Compute radii in the 3rd column.
# blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
# #%%

# blobs = np.array(blobs_log)
# x = blobs[:,0]
# y = blobs[:,1]
# plt.scatter(x, y)

# %%

#
# fig, ax = plt.subplots(1, 1, figsize=(14, 14))
# ax.set_title("Laplacian of Gaussian -- Blob")
# ax.imshow(image)
# for blob in blobs_log:
#     y, x, r = blob
#     c = plt.Circle((x, y), r, color='r', linewidth=2, fill=False)
#     ax.add_patch(c)
# ax.set_axis_off()
# plt.tight_layout()
# plt.show()

#%%
# Create an ImageJ gateway with the newest available version of ImageJ.
import imagej
ij = imagej.init()

# Load an image.
image_url = 'https://samples.fiji.sc/new-lenna.jpg'
jimage = ij.io().open(image_url)

# Convert the image from ImageJ to xarray, a package that adds
# labeled datasets to numpy (http://xarray.pydata.org/en/stable/).
img = ij.py.from_java(jimage)

# Display the image (backed by matplotlib).
ij.py.show(img, cmap='gray')
# %%
help(imagej)
# %%
