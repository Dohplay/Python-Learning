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
        
    return img

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
        
def solarize(img, threshold):
    """
    Solarize the specified image.
    """

    for x, y, col in img:

        # Invert the values of all RGB components less than 128,
        # leaving components with higher values unchanged.

        red, green, blue = col

        if red < threshold:
            red = 255 - red

        if green < threshold:
            green = 255 - green

        if blue < threshold:
            blue = 255 - blue

        col = create_color(red, green, blue)
        set_color(img, x, y, col)


#--------------------------------------
# A filter that uses an if-else statement.

def black_and_white(img):
    """
    Convert the specified image to a black-and-white (two-tone) image.
    """

    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on whether
    # its brightness is in the lower or upper half of this range.

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    for x, y, col in img:
        red, green, blue = col

        brightness = (red + green + blue) // 3
        if brightness < 128:
            set_color(img, x, y, black)
        else:     # brightness is between 128 and 255, inclusive
            set_color(img, x, y, white)


#--------------------------------------
# A filter that uses an if-elif-else statement.

def black_and_white_and_gray(img):
    """
    Convert the specified image to a black-and-white-and-gray
    (three-shade) image.
    """

    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of
    # pixels whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, col in img:
        red, green, blue = col
        brightness = (red + green + blue) // 3

        if brightness < 85:
            set_color(img, x, y, black)
        elif brightness < 171: # brightness is between 85 and 170, inclusive
            set_color(img, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(img, x, y, white)

def extreme_contrast(img):
    """
    Changes the components of each pixel
    """
    for x, y, col in img:
        red, green, blue = col
        
        if red < 128:
            red = 0
        else:
            red = 255
            
        if green < 128:
            green = 0
        else:
            green = 255
            
        if blue < 128:
            blue = 0
        else:
            blue = 255
            
        col = create_color(red, green, blue)
        set_color(img, x, y, col)
        
def sepia_tint(img):
    """
    tints image to sepia
    """
    
    img = grayscale(img)
    
    for x, y, col in img:
        red, green, blue = col
        if red < 63:
            blue *= 0.9
            red *= 1.1
        elif red >= 63 and red <= 191:
            blue *= 0.85
            red *= 1.15
        else:
            blue *= 0.93
            red *= 1.08
            
        col = create_color(red, green, blue)
        set_color(img, x, y, col)

def _adjust_component(amount):
    """
    helper function: returns the mid point between the 4 quadrants
    """
    
    if amount <= 63:
        return 31
    elif amount >= 64 and amount <= 127:
        return 95
    elif amount >= 128 and amount <= 191:
        return 159
    else:
        return 223
    
def posterize(img):
    """
    posterize the image, changes the components to the midpoint
    """
    
    for x, y, col in img:
        red, green, blue = col
        
        red = _adjust_component(red)
        green = _adjust_component(green)
        blue = _adjust_component(blue)
        
        col = create_color(red, green, blue)
        set_color(img, x, y, col)
        
def simplify(img):
    """
    changes image to white, black, or one of the three primary colours
    """
    
    for x, y, col in img:
        red, green, blue = col
        
        if red > 200 and green > 200 and blue > 200:
            col = create_color(255, 255, 255)
            set_color(img, x,y, col)
            
        elif red < 50 and green < 50 and blue < 50:
            col = create_color(0, 0, 0)
            set_color(img, x, y, col)
            
        else:
            if red > green and red > blue:
                col = create_color(255, 0, 0)
                set_color(img,x,y,col)
            
            elif green > red and green > blue:
                col = create_color(0,255,0)
                set_color(img,x,y,col)
                
            else:
                col = create_color(0,0,255)
                set_color(img,x,y,col)