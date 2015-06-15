import math

def quadratic_roots(a,b,c):
    """
    Formula returning the roots of a function given
    three values. Returns a tuple of the two roots of a
    quadratic equation.
    """
    positive_root = (-b + math.sqrt((b**2)-4*a*c))/(2*a)
    negative_root = (-b - math.sqrt((b**2)-4*a*c))/(2*a)
    return (positive_root, negative_root)

print (quadratic_roots(1, -4, -21))

def make_change(amount_due, amount_received):
    """
    Function that returns the value of payment and the
    value of change that is requried in return.
    """
    total = amount_received - amount_due
    loonie = total//100
    total %= 100
    quarter = total//25
    total %= 25
    dime = total//10
    
    
    total%= 10
    nickel = total//5
    total %= 5
    print ("Your change is %s loonies, %s quarters, %s dimes, %s nickel and \
    %s penny(s)" % (loonie, quarter, dime, nickel, total))
    return (loonie, quarter, dime, nickel, total)

print (make_change(100, 253))

def area_of_disk(r):
    """
    Returns the area of a ring with radius r.
    """
    return math.pi * r ** 2

def area_of_ring(outer,inner):
    """
    Returns the area of a ring with radius outer.
    The radius of the hole is inner.
    """
    return area_of_disk(outer) - area_of_disk(inner)

    
def circumference(radius):
    """
    calculates the circumference of the pipe
    """
    return 2*radius*math.pi

def area_of_pipe(inner_radius, length, thickness):
    """
    Calculates the area of a pipe and it's hallowed inside
    """
    surface_area = circumference(inner_radius+thickness)*length \
        + circumference(inner_radius)*length \
        + area_of_ring(inner_radius+thickness, inner_radius)*2
    return surface_area

print (area_of_pipe(2,3,4))
        
