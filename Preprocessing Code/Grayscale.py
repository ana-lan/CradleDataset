from PIL import Image
import os

# Set the directory where the images are located
img_dir = r'D:\cradle\Dataset\Cradle Dataset\Preprocessed\Normalized\sleeping'
save_dir = r'D:\cradle\Dataset\Cradle Dataset\Preprocessed\GrayScaled\sleeping'

# Loop through all the images in the directory
for filename in os.listdir(img_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):

        # Open the image
        img_path = os.path.join(img_dir, filename)
        img = Image.open(img_path)

        # Convert the image to grayscale
        gray_img = img.convert('L')

        # Save the grayscale image with "_gray" added to the filename
        gray_img_path = os.path.join(
            save_dir, filename.split('.')[0] + '_gray.png')
        gray_img.save(gray_img_path)
