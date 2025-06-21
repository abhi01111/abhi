n1 = int(input(f"Enter the 4 Digit Number : "))

def face_value(parameter):
    digit4 = ( parameter // 1000 ) % 10
    digit3 = (parameter // 100 ) % 10
    digit2 = (parameter // 10 ) % 10
    digit1 = parameter % 10

    return " {} {} {} {} ".format(digit4 ,digit3, digit2, digit1)

res = face_value(n1)
print(f"Face Value is {res}")

def place_value(parameter):
    digit1 = parameter % 10
    digit2 = (parameter //10) % 10
    digit3 = (parameter // 100 ) % 10
    digit4 = (parameter // 1000 ) % 10

res = place_value(n1)
print(f"Place Value is {res}")

def reverse_order(parameter):
    digit1 = parameter % 10
    digit2 = (parameter // 10) % 10
    digit3 = (parameter // 100) % 10
    digit4 = (parameter // 1000) % 10

    return "{} {} {} {}".format(digit1, digit2, digit3, digit4)

res_reverse = reverse_order(n1)
print(f"the number in Reverse order is {res_reverse}")