# 3. Write a Python program to convert a given list of integers and a tuple of
# integers into a list of strings. Use Python map.

def function():
    numbers = [1,2,3,4]
    num = 2,3,4,5

    numbers_str = list(map(str, numbers))
    num_str = list(map(str, num))

    print(f"list to string : {numbers_str}, type = {type(numbers_str)}")
    print(f"tuple to string :{num_str}, type = {type(num_str)}")

function()