Task
Create a function that always returns True for every item in a given list. However, if an element is the word "flick", switch to always returning the opposite boolean value.
Notes
* "flick" will always be given in lowercase.
* A list may contain multiple flicks.
* Switch the boolean value on the same element as the flick itself.




def flick_switch(lst):
    result = []
    switch = True
    for i in lst:
        if i == "flick":
            switch = not switch
        result.append(switch)
    
    return result