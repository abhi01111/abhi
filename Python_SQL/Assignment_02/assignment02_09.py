# write a function to return simple interest 
# To calculate simple interest, you can use the formula: SI = (P × R × T) / 100. In this formula,  
# • SI: Stands for simple interest 
# • P: Represents the principal amount 
# • R: Represents the interest rate per year 
# • T: Represents the time in years


def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter the Principal amount : "))
r = float(input("Enter the rate on amount : "))
t = float(input("Enter the time period : "))

SI = simple_interest(p, r, t)

print(f"Simple Interest is : {SI}")
