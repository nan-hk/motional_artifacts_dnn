import numpy as np
import os    # Traverse folders 
import nibabel as nib #nii Format 1 This bag will be used in general 
import imageio   # Convert to an image 
import re
from pathlib import Path

def nii_to_image(niifile):
 string1 = os.path.join(filepath, imgfile)
 string2 = re.sub("/", r"\\", string1)
 print('Hello', string2)
 filenames = list(Path(string2).glob('*.nii')) # Read nii Folder 
 slice_trans = []
 for f in filenames:
  # Start reading nii Documents 
  img_path = os.path.join(filepath, imgfile, f)
  img = nib.load(img_path)    # Read nii
  img_fdata = img.get_fdata()
  fname = str(f).replace('.nii','')   # Remove nii Suffix name of 
  img_f_path = os.path.join(filepath1, imgfile)
  # Create nii The folder of the corresponding image 
  if not os.path.exists(img_f_path):
   os.mkdir(img_f_path)    # New Folder 
 
  # Start converting to an image 
  (x,y,z) = img.shape
  for i in range(z):      #z Is a sequence of images 
   silce = img_fdata[:, :, i]   # You can choose which direction of slice 
   str1 = os.path.join(filepath1, img_f_path, fname + '{}.png'.format(i))
   str2 =  re.sub("/", r"\\", str1)
   imageio.imwrite(str2, silce)
   print(filepath1, img_f_path)
            # Save an image 
 
if __name__ == '__main__':
 imgs =['GT/', 'RGB/', 'depth/', 'depth_with_noise/']
 #imgs = ['depth/']
 for i in imgs:
  filepath = 'C:/nhk/Spring2022/-motion-artifacts/dataset/spnet_data_2D/spnet_data_3D_more_noise/TestDataset2/NLPR/'
  filepath1 = 'C:/nhk/Spring2022/-motion-artifacts/dataset/spnet_data_2D/spnet_data_3D_more_noise/TestDataset2/NLPR/'
  imgfile = i
  nii_to_image(filepath)

  print(i)