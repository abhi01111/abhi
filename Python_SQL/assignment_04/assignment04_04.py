# Write a Python program that calculates the sum of the squares of all odd
# numbers in a list of integers using map() and filter()
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = [1,2,3,4,5,6,7,8,9]
odd_numbers = filter(lambda n:n % 2 != 0, numbers)
square_odd = map(lambda n: n ** 2, odd_numbers)
sum_square = sum(square_odd)
print(f"sum of odd number is : {sum_square}")
