#Write a program that accepts a list from user and print the alternate element of list.

def function():
    num = list(map(int, input("Enter the numbers : ").split()))
    print(f"Numbers = {num}")
    print(f"Alternet elements of the list :")
    for i in range(0,len(num),2):

        print(num[i])

function()
