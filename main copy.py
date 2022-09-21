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
    rgb_image = image.convert('RGB')
    new_file_name = "/opt/icons/" + original_file_name[0] + '.jpg'
    rgb_image.save(new_file_name)

def image_resize(image):
    """resizes an image from 192x192 ---> 128x128"""
    image.resize((128, 128))

def image_rotate(image):
    """rotates an image 90 degrees clockwise"""
    image.rotate(90)

def main():

    #for loop to import files from the directory
    #path_of_images = "~\image-project\images\example.tiff"
    number_of_files_converted = 0
    for tiff in os.listdir("images"):
        original_file_name = os.path.splitext(tiff)
        with Image.open(os.path.join('images', tiff)) as image:
            image = image.resize((128, 128))
            image = image.rotate(90)
            rgb_image = image.convert('RGB')
            new_file_name = "/opt/icons/" + original_file_name[0] + '.jpg'
            rgb_image.save(new_file_name)
            number_of_files_converted += 1
    print(f"Files converted: {number_of_files_converted}")

main()
