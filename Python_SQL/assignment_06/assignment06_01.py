# 1. Create a class named Mobile with attributes ModelName,Company,Price and with
# methods:set_attributes, print_details and can_afford

class Mobile:
    def __init__(self,modelname,company,price):
        setattr(self, 'modelname', modelname)
        setattr(self, 'company', company)
        setattr(self, 'price', price)

    def print_details(self):
        print(f"Model name = {getattr(self, 'modelname')}")
        print(f"company = {getattr(self, 'company')}")
        print(f"price = {getattr(self, 'price')}")

    def can_afford(self):
        if getattr(self, 'price') > 20000:
            print(f"Can Afford ")
        else:
            print(f" can't afford ")

p1 = Mobile('y20', 'vivo', 25000)
p1.print_details()
p1.can_afford()

print('_' * 80)

p2 = Mobile('s24', 'samsung', 5000)
p2.print_details()
p2.can_afford()