import pydicom as dicom
import matplotlib.pyplot as plt
import pandas as pd
import PIL 
imgpath="image-00001.dcm"
ds=dicom.dcmread(imgpath)
plt.imshow(ds.pixel_array)
plt.show()