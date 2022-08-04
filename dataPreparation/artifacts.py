import os
import numpy as np
import nibabel as nib
from motion_corruption import load_image, manipulate_kspace_columns, image_reconstruction, write_image, generate_motion_trajectory

def main():
    input_dir = "/nhk/Spring2022/-motion-artifacts/dataset/spnet_data_2D/spnet_data_3D_more_noise/TestDataset2/DES/depth/"

    for root,dirs,filenames in os.walk(input_dir):
            print(root)
            for image in sorted(filenames):
                imageName = image
                filepath = os.path.join(root, image)
                if '.nii' in filepath: 
                    image, array = load_image(filepath)
                    imagesize = image.GetSize()
                    print(filepath)
                    print(imagesize)
                    motion_table=generate_motion_trajectory(imagesize)
                    np.save(root+'/motion_table',motion_table)
                    corrupted_data = manipulate_kspace_columns(motion_table,filepath,imagesize)
                    corrupted_image = image_reconstruction(corrupted_data)
                    write_image(root,corrupted_image, imageName)

if __name__ == "__main__": 
    main()