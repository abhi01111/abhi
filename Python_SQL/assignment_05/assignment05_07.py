# 7) Write a program to read 6 numbers and create a dictionary having keys EVEN
# and ODD.
# Dictionary's value should be stored in list. Your dictionary should be like:
# {'EVEN':[8,10,64], 'ODD':[1,5,9]}

keys = {
    "EVEN" : [],
    "ODD" : []
}

for i in range(6):
    num = int(input(f"Enter the Element : "))
    if num % 2 == 0:
        keys["EVEN"].append(num)
    else:
        keys["ODD"].append(num)

print(keys)