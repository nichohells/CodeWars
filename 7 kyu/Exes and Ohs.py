Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.




def xo(s):
    count_x = 0
    count_o = 0
    for char in s.lower():
        if char == "x":
            count_x += 1
        elif char == "o":
            count_o += 1
    if count_x == count_o:
        return True
    else:
        return False
    return count_x, count_o