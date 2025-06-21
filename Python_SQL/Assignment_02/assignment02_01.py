def cube(n):
    return n ** 3

n1 = float(input("Enter the first number : "))
n2 = float(input("Enter the Second Number : "))
n3 = float(input("Enter the third numer : "))
n4 = float(input("Enter the Fourth Number : "))
n5 = float(input("Enter the Fifth number : "))

sum_of_cubes = cube(n1) + cube(n2) + cube(n3) + cube(n4) + cube(n5)

print(f"Sum of Cube is : {sum_of_cubes}, data type = {type(sum_of_cubes)}")