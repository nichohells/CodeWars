Complete the function which will return the area of a circle with the given radius.
Returned value is expected to be accurate up to tolerance of 0.01.
If the radius is not positive, raise ValueError.




def circle_area(r):
    if r <= 0:
        raise ValueError
    
    area = (22 / 7) * (r ** 2)
    return area