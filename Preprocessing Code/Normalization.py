import cv2
import numpy as np
import os


def normalize_images(images_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Loop through all the images in the input directory
    for image_file in os.listdir(images_path):
        image_path = os.path.join(images_path, image_file)

        # Load the image using OpenCV
        image = cv2.imread(image_path)

        # Resize the image to the desired size
        if image is None:
            print('Wrong path:', images_path)
        else:
            image = cv2.resize(image, dsize=(128, 128))

        # Convert the image to floating point format and normalize the pixel values to [0,1]
        image = image.astype(np.float32) / 255.0

        # Save the normalized image to the output directory
        output_file = os.path.join(output_path, image_file)
        # convert back to 8-bit format before saving
        cv2.imwrite(output_file, image * 255.0)

    print("Image normalization complete!")


# Example usage: normalize all images in a directory and save them to a new directory
images_path = r'D:\cradle\Dataset\Cradle Dataset\Original\sleeping'
output_path = r'D:\cradle\Dataset\Cradle Dataset\Preprocessed\Normalized\sleeping'
normalize_images(images_path, output_path)
