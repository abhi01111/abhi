length = int(input("Enter the length of rectangle : "))
width = int(input("Enter the width of rectangle : "))

def area_of_rectangle(length, width):
    return length * width

def peri_of_rectangle(length, width):
    return (length + width) * 2

area = area_of_rectangle(length, width)
peri = peri_of_rectangle(length, width)

print(f"area = {area}, type{type(area)}")
print(f"peri = {peri}, type = {type(peri)}")