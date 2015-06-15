from math import *

def distance(pt1, pt2):
    distance = (sqrt((pt2[0] - pt1[0])**2 + (pt2[1] - pt1[1])**2))
    return distance

def curveFitting(points):   
    sumx = 0
    sumy = 0
    n = len(points)
    sumxx = 0
    sumyy = 0
    sumxy = 0
    
    for point in points:
        x, y = point
        sumx += x
        sumy += y
        sumxx += x**2
        sumyy += y**2
        sumxy += x*y
        
        m = (sumx*sumy - n*sumxy)/(sumx*sumx - n*sumxx)
        b = (sumx*sumxy - sumxx*sumy)/(sumx*sumx-n*sumxx)

    return m, b

