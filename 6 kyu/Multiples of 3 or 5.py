If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
Note: If the number is a multiple of both 3 and 5, only count it once.
#if a number is a multiple of 3, the sum of the individual digits in the number is al os a multiple of 3
#multiples of 5 are all numbers that end in either 5 or 0
limit = 0


def solution(limit):
    result = 0
    for number in range(limit):
        if (number % 3 == 0 or number % 5 == 0):
            result += number
    return result
    
solution(limit)