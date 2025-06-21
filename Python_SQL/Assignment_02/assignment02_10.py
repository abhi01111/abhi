def compound_interest(p, r, n, t):
    return p * (1 + (r/n)) ** n * t

p = float(input("Enter the Principal Amount : "))
r = float(input("Enter the rate : "))
n = float(input("Enter the interest : "))
t = float(input("Enter the time period : "))

CI = compound_interest(p, r, n, t)

print(f"Compound Interest = {CI}")