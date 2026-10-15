import math

"""
Assignment 1:
Create a function that takes 2 parameters that are integers.  The function will return both the greatest common factor as well as the lowest common multiple.  You will likely need some other functions to help you accomplish this task.
Some ideas (you don't have to use them):
* a function that takes 1 parameter that is an integer.  The function will return a list of the factors for that number
* a function that takes 2 lists and determines the largest number that is common to both sets
"""
def factors(number):
    # number is an integer value
    # you will likely need to sort the values of your list
    answer = []
    for i in range(1, number + 1):
        if number % i == 0:
            answer.append(i)
    return answer

def gcflcm(n1,n2):
    gcf = -1
    lcm = -1

    factors_n1 = factors(n1)
    factors_n2 = factors(n2)
    for factor in factors_n1:
        if factor in factors_n2:
            gcf = factor
    lcm = (n1 * n2) // gcf
    return gcf,lcm

assert factors(12) == [1,2,3,4,6,12]
assert factors(20) == [1,2,4,5,10,20]
assert factors(16) == [1,2,4,8,16]
assert factors(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]

assert gcflcm(3,3) == (3,3)
assert gcflcm(24,16) == (8,48)
assert gcflcm(12,30) == (6,60)
assert gcflcm(250,1480) == (10,37000)

