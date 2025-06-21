#  Write a Python program that adds two lists element-wise using the map()
# function.
# input :   list1 = [1, 2, 3, 4, 5]
# list2 = [5, 4, 3, 2, 1]
# Expected Output  : [6, 6, 6, 6, 6]
from python.python.program1 import addition, answers


def function():
    p1 = [1,2,3,4,5]
    p2 = [5,4,3,2,1]

    print(f"List 1 = {p1}")
    print(f"List 2 = {p2}")

    result = list(map(lambda n,m: n+ m ,p1, p2))

    print(f"List = {result}")

function()
