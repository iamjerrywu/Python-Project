"""
File: blur.py
Name: sheng-hao wu
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return: new(blurred) img
    """
    #create new image
    new_img = SimpleImage.blank(img.width, img.height)

    sum_red, sum_green, sum_blue, count = 0, 0, 0, 0
    # frame = 3 x 3, [[x_left_bnd, x_right_bnd], [y_low_bnd, y_up_bnd]]
    frame = [[-1, 2], [-1, 2]]

    for x in range(img.width):
        for y in range(img.height):
            for frame_x in range(frame[0][0], frame[0][1]):
                for frame_y in range(frame[1][0], frame[1][1]):
                    if (img.width > x + frame_x >= 0 ) & (img.height > y + frame_y >= 0):
                        # get old img pixel
                        img_pixel = img.get_pixel(x + frame_x, y + frame_y)
                        # calculate RGB sum
                        sum_red+=img_pixel.red
                        sum_green+=img_pixel.green
                        sum_blue+=img_pixel.blue
                        count+=1
            # average RGB and assign to new image
            new_img.set_rgb(x, y, sum_red//count, sum_green//count, sum_blue//count)

            # reset RGB sum and count
            sum_red, sum_green, sum_blue, count = 0, 0, 0, 0
    return new_img

def main():

    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()

if __name__ == '__main__':
    main()
