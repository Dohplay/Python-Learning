# SYSC 1005 Fall 2014

from Cimpl import *

def blur(source):
    """
    Return a new image that is a blurred copy of the image bound to source.
    """

    # We modify a copy of the original image, because we don't want blurred
    # pixels to affect the blurring of subsequent pixels.
    
    target = copy(source)
    
    # Notice the arguments passed to range(). We don't want to modify the
    # pixels at the image's edges.

    for y in range(1, get_height(source) - 1):
        for x in range(1, get_width(source) - 1):

            # Grab the pixel @(x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(source, x, y - 1)
            left_red, left_green, left_blue = get_color(source, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(source, x, y + 1)
            right_red, right_green, right_blue = get_color(source, x + 1, y)
            center_red, center_green, center_blue = get_color(source, x, y)

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red ) // 5

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green +
                                   right_green + center_green ) // 5

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                                   right_blue + center_blue ) // 5

            # Blur the pixel @(x, y) in the copy of the image
            new_color = create_color(new_red, new_green, new_blue)
            set_color(target, x, y, new_color)

    return target


def test_blur():
    original = load_image(choose_file())
    blurred = blur(original)
    show(original)
    show(blurred)
    save_as(blurred, "blurred.jpg")
    
    
def make_very_blurry(number_of_blurs):
    img = load_image(choose_file())
    
    for i in range(number_of_blurs):
        img = blur(img)  # Blur the image repeatedly

    show(img)
    save_as(img, "very_blurred.jpg")   
    
    
# Exercise - modify the filter so that it averages the components of
# the pixel @(x, y) and its eight neigbours. Use nested for loops to get 
# the RGB components from the 9 pixels and sum them; in other words, don't
# use 9 statements of the form:
#
#   top_red, top_green, top_blue = get_color(source, x, y - 1)
#   ... 
#
# followed by:
# 
#   new_red = (top_red + ... + center_red ) // 9
#   ...
#
#
# Exercise - modify the filters so that the pixels at the image's edges are
# blurred. Hint: the number of neighbours will vary, depending on the 
# pixel's coordinates.