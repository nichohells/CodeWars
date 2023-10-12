In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.
The result should also be ordered from highest to lowest.




def two_highest(arg1):
    if len(arg1) == 0:
        return [] 
    unique_values = list(set(arg1))
    if len(unique_values) < 2:
        return unique_values 
    first_highest = max(unique_values)
    unique_values.remove(first_highest)
    second_highest = max(unique_values)
    return [first_highest, second_highest]