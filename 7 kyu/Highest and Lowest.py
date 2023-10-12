In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
Notes
* All numbers are valid Int32, no need to validate them.
* There will always be at least one number in the input string.
* Output string must be two numbers separated by a single space, and highest number is first.




def high_and_low(numbers):
    num_list = [int(num) for num in numbers.split()]
    highest = max(num_list)
    lowest = min(num_list)
    return str(highest) + " " + str(lowest)