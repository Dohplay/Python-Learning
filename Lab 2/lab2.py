import math

def area_of_disk(r):
    """
    Returns the area of a ring with radius r.
    """
    return math.pi * r ** 2

def area_of_ring(outer,inner):
    """
    Returns the area of a ring withr adius outer.
    The radius of the whole is inner.
    """
    return area_of_disk(outer) - area_of_disk(inner)

print (area_of_disk(5))
print (area_of_ring(10,5))

def area_of_cone(h,r):
    """
    Returns the lateral surface are of a right circular
    cone with height h and radius r
    """
    return math.pi*r*(math.sqrt(r**2 + h**2))

print (area_of_cone(2,2))

def volume_of_sphere(r):
    """
    Returns the volume of a sphere
    """
    return (4/3)*(math.pi)*(r**3)

print (volume_of_sphere(2))

def hollow_sphere(r_large_sphere, r_small_sphere):
    """
    Returns the volume of a hollow sphere
    """
    return volume_of_sphere(r_large_sphere) - volume_of_sphere(r_small_sphere)

print (abs(hollow_sphere(4,5)))
    