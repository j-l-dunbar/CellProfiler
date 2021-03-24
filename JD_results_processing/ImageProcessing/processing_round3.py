#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  matplotlib.image as img
import skimage as ski


from skimage.filters import unsharp_mask
from scipy.signal import convolve2d as conv2
from skimage import color, data, restoration
from skimage.color import rgb2gray
import psf
image = img.imread("Adt_ret_EphA5-Efna5-EphA6_JD12_s3c4.tif")
image.shape
cropped = image[6300:7300,5000:6500]
BandW = rgb2gray(cropped)


def subtract_background(image, radius=100, light_bg=False):
        from skimage.morphology import white_tophat, black_tophat, disk
        str_el = disk(radius) #you can also use 'ball' here to get a slightly smoother result at the cost of increased computing time
        if light_bg:
            return black_tophat(image, str_el)
        else:
            return white_tophat(image, str_el)



# %%
nimus_BG = subtract_background(BandW)
fig, ax = plt.subplots(figsize=(14,14))
ax.imshow(nimus_BG)
# %%
