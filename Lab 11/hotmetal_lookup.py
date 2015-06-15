from Cimpl import *

def build_hot_metal_lookup_table():
    """
    Builds a lookup table for the hot metal filter
    """
    lookup = list()
    
    for c in range(256):
        lookup.append(c)
    return lookup

hot_metal_table = build_hot_metal_lookup_table()

def hot_metal(img, table):
    """
    Overlays the defined image with a 'hot metal' filter
    """
    for x in range(get_width(img)):
        for y in range(get_height(img)):
            slopeR = 255/170
            slopeG = 255/85            
            r,g,b = get_color(img,x,y)
            weighted_brightness = 0.3*r + 0.59*g + 0.11*b
            
            if weighted_brightness <= 170:
                r = table[int(weighted_brightness*slopeR)]
                g = 0
            else:
                r = 255
                g = table[int((weighted_brightness-170)*slopeG)]
            b = 0
            
            col = create_color(r,g,b)
            set_color(img,x,y, col)

img = load_image(choose_file())
hot_metal(img,hot_metal_table)
show(img)
            