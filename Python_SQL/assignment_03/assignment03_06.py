#  Find and display the largest number of a list without using built-in function
# max(). Your program should ask the user to input values in list from keyboard.

a = int(input("Enter the value : "))
b = int(input("Enter the value : "))
c = int(input("Enter the value : "))
list = []
def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(f"Maximum number is {largest(a, b, c)}")
