# Write a Python function to find the maximum of three numbers.
def find_max(n1, n2, n3):
    return max(n1, n2, n3)

n1 = float(input("Enter the first number : "))
n2 = float(input("Enter the Second NUmber : "))
n3 = float(input("Enter the Third Number : "))

max = find_max(n1, n2, n3)

print(f"Maximum Number is : {max} , data type = {type(max)}")
