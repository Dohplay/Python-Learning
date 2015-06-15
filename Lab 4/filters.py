""" SYSC 1005 A Fall 2014 Lab 4 - Part 3.
"""

from Cimpl import *

#--------------------------------------
# This function was presented in class:

img = load_image(choose_file())

def grayscale(img):
    """
    Convert the specified picture into a grayscale image.
    """

    for pixel in img:
        x, y, col = pixel
        r, g, b = col

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        
        set_color(img, x, y, gray)

def negative(img):
    """
    make image negative
    """
    for pixel in img:
        x, y, col = pixel
        r, g, b = col
    
        r = 255-r
        g = 255-g
        b = 255-b
        
        col = create_color(r,g,b)
        set_color(img, x, y, col)
    
    
def weighted_grayscale(img):
    """
    Convert the specified picture into a weighted grayscale image.
    """
    for pixel in img:
        x, y, col = pixel
        r, g, b = col

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = r*0.299 + g*0.587 + b*0.114
        gray = create_color(brightness, brightness, brightness)
        
        set_color(img, x, y, gray)
