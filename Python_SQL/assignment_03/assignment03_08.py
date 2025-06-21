# Write a program that will calculate the price for a quantity entered from the
# keyboard, given that the unit price is Rs 5 and there is a discount of 10 percent
# for quantities over 30 and a 15 percent discount for quantities over 50.

quantity = int(input(f"Enter the quantity : "))
def discount():
    if quantity <= 30 :
        print(f"discount = {quantity * 5}")
    elif quantity >= 30 and quantity <= 50 :
        print(f"Discount = {(quantity * 5) * (1 / 10)}")
    elif quantity > 50 :
        print(f"Discount = {(quantity * 5) * (15 / 100)}")
    else:
        print("Product is not available")


discount()
