# """Write a program that will calculate the price for a quantity entered from the
# keyboard, given that the unit price is Rs 5 and there is a discount of 10 percent
#  for quantities over 30 and a 15 percent discount for qu antities over 50."""


Quantity = int(input(f"Enter the Quantity : "))

def price_with_discount():
    if Quantity <= 30:
        print(f"Price of the Quantity is {Quantity * 5}")
    elif Quantity >= 30 and Quantity <= 50:
        print(f"Price of the Quantity with 10 percent discount is {(Quantity * 5) * 0.1}")
    elif Quantity >= 50:
        print(f"Price of the Quantity with 15 percent discount is {(Quantity * 5) * 1.5}")
    else:
        print(f"Dont purchase save money")


price_with_discount()
