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
                
                
def detect_edges(img, threshold):
    """
    Detects edges by comparing pixel above and below
    """
    for y in range(get_height(img)  - 1):
        for x in range(get_width(img)):
            pixelAbove = get_color(img, x, y)
            red, green, blue = pixelAbove
            contrastAbove = (red + green + blue)/3
            pixelBelow = get_color(img, x, y+1)
            red, green, blue = pixelBelow
            contrastBelow = (red + green + blue)/3
            
            difference = abs(contrastAbove - contrastBelow)
            
            if difference > threshold:
                black = create_color(0,0,0)
                set_color(img, x, y, black)
            else:
                white = create_color(255,255,255)
                set_color(img, x, y, white)

def detect_edges_better(img, threshold):
    """
    Detects edges by comparing the pixel above, below, and to the right
    """
    
    for y in range(get_height(img)  - 1):
        for x in range(get_width(img) - 1):
            pixelAbove = get_color(img, x, y)
            red, green, blue = pixelAbove
            contrastAbove = (red + green + blue)/3
            
            pixelBelow = get_color(img, x, y+1)
            red, green, blue = pixelBelow
            contrastBelow = (red + green + blue)/3
            
            pixelRight = get_color(img, x+1, y)
            red, green, blue = pixelRight
            contrastRight = (red + green + blue)/3
            
            difference = abs(contrastAbove - contrastBelow - contrastRight)
            
            if abs(contrastAbove - contrastBelow) > threshold or \
            abs(contrastAbove - contrastRight) > threshold:
                black = create_color(0,0,0)
                set_color(img, x, y, black)
            else:
                white = create_color(255,255,255)
                set_color(img, x, y, white)

def blur(source):
    """
    Return a new image that is a blurred copy of the image bound to source.
    """

    # We modify a copy of the original image, because we don't want blurred
    # pixels to affect the blurring of subsequent pixels.
    
    target = copy(source)
    
    # Notice the arguments passed to range(). We don't want to modify the
    # pixels at the image's edges.
    
    for y in range(1, get_height(source)-1):      
        for x in range(1, get_width(source)-1):
            new_red = 0
            new_green = 0
            new_blue = 0            
            for y1 in range(y-1, y+2):
                for x1 in range(x-1, x+2):
                    pixel = get_color(source, x1, y1)
                    red,green, blue = pixel
                    new_red += red
                    new_green += green
                    new_blue += blue
                    new_color = create_color(new_red//9, new_green//9, new_blue//9)
                    set_color(target,x,y,new_color)
            """    
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
            """
            

    return target

def flip(img):
    target = copy(img)
    for y in range(1, get_height(img)):
        for x in range(1, get_width(img)):
            pixelCol = get_color(img, x, y)
            red, green, blue = pixelCol
            pixelX = (get_width(img) - x)
            pixelCol2 = get_color(img,pixelX, y)
            red1, green1, blue1 = pixelCol2
            
            set_color(target, x, y, pixelCol2)
            set_color(target, pixelX, y, pixelCol)
    return target
            