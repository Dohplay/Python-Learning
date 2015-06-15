"""
SYSC 1005 Fall 2014 Lab 9, Parts 2 and 3
"""

from points import *

def get_points():
    """ Return a set of (x, y) points, with each point stored in a tuple.
    """
    return {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}


def fit_line_to_points(points):
    slope_and_intercept = curveFitting(points)
    return slope_and_intercept

def read_and_print_lines():
    infile = open("data.txt", "r")
    for line in infile:
        print(line)
    infile.close()

def read_points(filename):
    numbers = set()
    lines = open(filename, "r")
    for line in lines:
        number = line.split()
        x, y = number
        numbers.add((float(x), float(y)))
    lines.close()
    return numbers

if __name__ == "__main__":
    points = input("input file name: ")
    value = read_points(points)
    slope = fit_line_to_points(value)[0]
    intercept = fit_line_to_points(value)[1]
    print("The best-fit line is y = %sx + %s" % (slope, intercept))
    


