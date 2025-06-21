# 7. Write a Python program that filters out numbers greater than 10 from a list
# of numbers using the filter() function.
# Input: numbers = [5, 12, 3, 18, 9, 20, 22, 21]
# Output: [12, 18, 20, 22, 21]

def function():
    numbers = [5,12,3,18,9,20,22,21]
    print(f"Numbers = {numbers}")

    num_greater = list(filter(lambda n: n > 10 , numbers))
    print(f"Greater Numbers are = {num_greater}")

function()