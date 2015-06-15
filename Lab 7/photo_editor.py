# SYSC 1005 A Fall 2014 Lab 7
# Revised: November 3, 2014.

import sys  # get_image calls exit
from Cimpl import *
from filters import *

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img

if __name__ == "__main__":
    done = False
    loaded = False
    # A bit of code to demonstrate how to use get_image().
    while done == False:
        prompt = str(input("Load an image," \
                            "Make an image Negative, "\
                            "Make an image Grayscale, " \
                            "Make an image Posterized, \n" \
                            "Make an image Sepia Tint, " \
                            "Detect the edges of an image, " \
                            "Quit (L, N, G, P, S, E, Q):"\
                            )).upper()
        if prompt in ["N", "G", "P", "S", "E"]\
            and loaded == False:
            print("There is no currently Loaded Image to execute this command.\
            \nPlease try again.\n")
        else:
            if prompt == 'L':
                img = get_image()
                loaded = True
            elif prompt == 'N':
                img = negative(img)
                show(img)
            elif prompt == "G":
                img = grayscale(img)
                show(img)
            elif prompt == "P":
                img = posterize(img)
                show(img)
            elif prompt == "S":
                img = sepia_tint(img)
                show(img)
            elif prompt == "E":
                threshold = int(input("What is the threshold?"))
                img = detect_edges_better(img, threshold)
                show (img)
            elif prompt == 'Q':
                print("Exiting Program")
                done = True
            else:
                print("Not a valid input command. Please try again.")