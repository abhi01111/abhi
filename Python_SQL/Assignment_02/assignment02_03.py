# write a program to find given number is positive ,nigetive or zero.
number = int(input("Enter the number : "))

res = {True: "Positive" , False: {True: "Negative" , False: "Zero"}}

print(f"The Number is {res[number > 0] if number != 0 else res[False][False]}")
