# . Write a Python program to double all numbers in a given list of integers. Use
# Python map, lambda function.
# list1 = [1,2,3,4,5,6,7,8,9]

def function():
    numbers = [1,2,3,4,5,6,7,8,9]

    make_double = lambda n: n + n

    double = list(map(make_double, numbers))

    print(f"number = {numbers}")
    print(f"double = {double}")

function()