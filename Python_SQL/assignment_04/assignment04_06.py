# 6. Write a Python program that filters out all strings that have more than 5
# characters from a list of strings using the filter() function.
# Input: words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange']
# Output: ['Yellow', 'Purple', 'Orange']

def function():
    words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange']
    result = list(filter(lambda word: len(word) > 5 , words))
    print(f"{result}")

function()