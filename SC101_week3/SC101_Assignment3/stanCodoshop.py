"""
File: stanCodoshop.py
Name: Sheng-Hao Wu
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

"""

import os
import sys
import math
from simpleimage import SimpleImage
from simpleimage import Pixel


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    # square root function to calculate RGB's color distance
    return math.sqrt((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    pixel_sum = [0, 0, 0]
    for pixel in pixels:
        # accumulate pixel R/G/B' value sum
        pixel_sum[0] += pixel.red
        pixel_sum[1] += pixel.green
        pixel_sum[2] += pixel.blue
    # return the average of R/G/B value
    return [color_sum//len(pixels) for color_sum in pixel_sum]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    # get RGB average values
    avg = get_average(pixels)
    # init minimum color distance (largest as 255)
    min_dist = 255
    # init minimum pixel
    min_pixel = Pixel(SimpleImage.blank(20, 20), 0, 0)

    # traverse pixels
    for pixel in pixels:
        # comparison for the pixel that has minimum color distance
        if min_dist > get_pixel_dist(pixel, avg[0], avg[1], avg[2]):
            min_dist = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
            min_pixel = pixel
    return min_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    # since every image in a series are in the same size
    # init image width/height with the first image
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # traverse all the image point from x:width to y:height
    for x in range(width):
        for y in range(height):
            # list to store those images' pixel in (x,y)
            img_pixel_list = []
            for img in images:
                # append each image pixel at (x,y) into empty list
                img_pixel_list.append(img.get_pixel(x, y))
            # calculate (x,y) best pixel (with minimum color distance)
            best_pixel = get_best_pixel(img_pixel_list)
            # set best pixel on result's (x,y) position
            result.set_pixel(x, y, best_pixel)
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
