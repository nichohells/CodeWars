In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.


def filter_list(l):
    new_list = []
    for char in l:
        if isinstance(char, int) and char >= 0:
            new_list.append(char)  
    return new_list