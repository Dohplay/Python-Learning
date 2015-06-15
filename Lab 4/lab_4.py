""" SYSC 1005 A Fall 2014 Lab 4 - Parts 1 and 2
Image processing examples.

D.L.Bailey, SCE, Carleton University
"""

from Cimpl import *

#---------------------------------------------
#
# These two functions were presented in class:

# maximize_red is used in Part 1, Exercise 1

img = load_image(choose_file())

def maximize_red(img):
   """ Modify the photo bound to img to look like it was taken at 
   sunset, by maximizing the red component of every pixel.
   """
   for pixel in img:
      x, y, col = pixel
      r, g, b = col
      new_color = create_color(255, g, b)
      set_color(img, x, y, new_color)
      
# make_sunset is used in Part 2, Exercise 3      

def make_sunset(img):
   """ Modify the photo bound to img to look like it was taken at 
   sunset, by reducing the green and blue components of every pixel.
   """
   for pixel in img:
      x, y, col = pixel  
      r, g, b = col

      g = g * 0.7 # decrease green by 30%
      b = b * 0.7 # decrease blue by 30%

      col = create_color(r, g, b)
      set_color(img, x, y, col)

def red_channel(img):
   """
   Set green and blue components to 0 , leave red component unchanged
   """
   for pixel in img:
      x, y, col = pixel
      r, g, b = col
      g = 0
      b = 0
      col = create_color(r,g,b)
      set_color(img,x,y,col)
      
def green_channel(img):
   """
   Set red and blue components to 0, leave green unchanged
   """
   for pixel in img:
      x, y, col = pixel
      r, g, b = col
      
      r = 0
      b = 0

      col = create_color(r,g,b)
      set_color(img, x,y, col)
      
def blue_channel(img):
   """
   set red and green components to 0, leave blue unchanged
   """
   for pixel in img:
      x, y, col = pixel 
      r, g, b = col
      
      r = 0
      g = 0
      
      col = create_color(r,g,b)
      set_color(img, x, y, col)
   
def halve_brightness(img):
   """
   halves the brightness of the image
   """
   for pixel in img:
      x, y, col = pixel
      r, g, b = col
      
      r *= 0.5
      g *= 0.5
      b *= 0.5
      
      col = create_color (r, g, b)
      set_color(img, x, y, col)
      
def swap_red_blue(img):
   """
   swaps red and blue components
   """
   for pixel in img:
      x, y, col = pixel
      b, g, r = col
      
      col = create_color(r,g,b)
      set_color(img, x ,y, col)
      
