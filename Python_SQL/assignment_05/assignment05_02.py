# 2) Write a program to sum all the values of a dictionary.
# Hint dict1 = {‘key 1’: 200, ‘key 2’: 300}
# Expected output
# Result: 500


def function():
    dict = {
        "key1" : 200,
        "key2" : 300
    }
    result = 0
    for sum in dict.values():
        result += sum
    print(f"sum = {result}")


function()