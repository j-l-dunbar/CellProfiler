#%%

import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np 
# import scipy
import skimage


# csv_c2 = pd.read_csv("RNAquant_Objects_C2.csv")
# print(f"C2 #Objects: {len(csv_c2)}")
csv_c3 = pd.read_csv("RNAquant_Objects_C3.csv")
print(f"C3 #Objects: {len(csv_c3)}")
csv_c4 = pd.read_csv("RNAquant_Objects_C4.csv")
print(f"C4 #Objects: {len(csv_c4)}")
# %%
EphA6 = csv_c2[['Location_Center_X','Location_Center_Y', 'AreaShape_Area', 
                'Intensity_MeanIntensity_c2', 'Intensity_MedianIntensity_c2','Intensity_IntegratedIntensity_c2',
                'ImageNumber', 'ObjectNumber', 'Metadata_Age', 'Metadata_ImageID', 'Metadata_ImageID.1',
                'Metadata_ImageInfo', 
                'AreaShape_MeanRadius', 'AreaShape_MedianRadius', 'AreaShape_MajorAxisLength','AreaShape_MinorAxisLength',]]
EphA6.rename(columns={'Location_Center_X':"X",'Location_Center_Y':"Y",'AreaShape_Area':"Area"}, inplace=True)

efnA5 = csv_c3[['Location_Center_X','Location_Center_Y', 'AreaShape_Area', 
                'Intensity_MeanIntensity_c3', 'Intensity_MedianIntensity_c3','Intensity_IntegratedIntensity_c3',
                'ImageNumber', 'ObjectNumber', 'Metadata_Age', 'Metadata_ImageID', 'Metadata_ImageID.1',
                'Metadata_ImageInfo', 
                'AreaShape_MeanRadius', 'AreaShape_MedianRadius', 'AreaShape_MajorAxisLength','AreaShape_MinorAxisLength',]]
efnA5.rename(columns={'Location_Center_X':"X",'Location_Center_Y':"Y",'AreaShape_Area':"Area"}, inplace=True)

EphA5 = csv_c4[['Location_Center_X','Location_Center_Y', 'AreaShape_Area', 
                'Intensity_MeanIntensity_c4', 'Intensity_MedianIntensity_c4','Intensity_IntegratedIntensity_c4',
                'ImageNumber', 'ObjectNumber', 'Metadata_Age', 'Metadata_ImageID', 'Metadata_ImageID.1',
                'Metadata_ImageInfo', 
                'AreaShape_MeanRadius', 'AreaShape_MedianRadius', 'AreaShape_MajorAxisLength','AreaShape_MinorAxisLength',]]
EphA5.rename(columns={'Location_Center_X':"X",'Location_Center_Y':"Y",'AreaShape_Area':"Area"}, inplace=True)


# %%

plt.scatter(efnA5.X, efnA5.Y)
plt.scatter(EphA5.X, EphA5.Y)

plt.show()
# %%

# %%
