# Write a program to find index of element ‘e’ in given
# vowels list [’a’, ’e’, ’i’,’o’, ’i’, ’u’]
from feb27.feb27.code.assignment03_03 import index

list = ['a', 'e', 'i', 'o', 'i', 'u']

print(f"list = {list}")

char = input(f"Enter the character : ")
if char in list:
    index = list.index(char)
    print(f"{index}")
else:
    print(f"character nt found.")




print(f"index = {index}")