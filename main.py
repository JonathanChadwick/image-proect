from PIL import Image
import os

# Original file formats:
#   - .tiff
#   - 192x192
#   - 90 degrees anti-clockwise <--

# Converted format:
#   - .jpeg
#   - 128 x 128
#   - Straight


def tiff_to_jpeg(image, original_file_name):
    """converts .tiff image to a .jpeg image"""
    new_file_name = original_file_name + '.jpg'
    image.save(new_file_name)

def image_resize(image):
    """resizes an image from 192x192 ---> 128x128"""
    image.resize((128, 128))

def image_rotate(image):
    """rotates an image 90 degrees clockwise"""
    image.rotate(90)

def main():

    #for loop to import files from the directory
    path_of_images = "\image-project\images"
    number_of_files_converted = 0
    for tiff in os.listdir(path_of_images):
        original_file_name = os.path.splitext(tiff)
        with Image.open(tiff) as image:
            tiff_to_jpeg(image, original_file_name)
            image_resize(image)
            image_rotate(image)
            number_of_files_converted += 1
    print(f"Files converted: {number_of_files_converted}")
