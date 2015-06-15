# SYSC 1005 Fall 2014
# Image processing filters that use nested loops to work on a range of pixels.

from Cimpl import *

def grayscale(img):
    """
    Convert the specified image into a grayscale image.
    """

    for y in range(get_height(img)):
        for x in range(get_width(img)):

            # Use the shade of gray that has the same brightness as the pixel's
            # original color.

            r, g, b = get_color(img, x, y)
            brightness = (r + g + b) // 3
            gray = create_color(brightness, brightness, brightness)
            set_color(img, x, y, gray)
            

def three_bands(img):
    """ 
    Modify the specified image to have three horizontal bands. The upper
    third is coloured in shades of red, the middle band is coloured in
    shades of green, and the lower band is coloured in shades of blue.
    """
    
    height = get_height(img)

    # Modify the upper third of the image.
    
    for y in range(height // 3):
        for x in range(get_width(img)):

            r, g, b = get_color(img, x, y)
            avg = (r + g + b) // 3
            col = create_color(avg, 0, 0) # a shade of red
            
            # could combine the previous two statements:
            # col = create_color((r + g + b) // 3, 0, 0)
            
            set_color(img, x, y, col)
            
    # Modify the middle third of the image.
    
    for y in range(height // 3, 2 * height // 3):
        for x in range(get_width(img)):

            r, g, b = get_color(img, x, y)
            avg = (r + g + b) // 3
            col = create_color(0, avg, 0) # a shade of green
            set_color(img, x, y, col)
            
    # Modify the lower third of the image.

    for y in range(2 * height // 3, height):
        for x in range(get_width(img)):

            r, g, b = get_color(img, x, y)
            avg = (r + g + b) // 3
            col = create_color(0, 0, avg) # a shade of blue
            set_color(img, x, y, col)

def test_grayscale():
    img = load_image(choose_file())
    grayscale(img)
    show(img)

def test_three_bands():
    img = load_image(choose_file())
    three_bands(img)  
    show(img)