from math import *

def polysum(n, s):
    """ 
    input: n = number of sides, s = length of side
    function sums the area and square of the perimeter of the regular polygon
    returns the sum, rounded to 4 decimal places."""

    area = (0.25 * n * s**2) / tan(pi / n)
    perimeter = n * s
    sum_area_perimeter = area + perimeter**2
    return round(sum_area_perimeter, 4)