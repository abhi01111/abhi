to_fahrenheit = lambda f:(f * (9 / 5)) + 32
temp_in_fahrenheit = to_fahrenheit(50)
print(f"Temperature in Fahrenheit = {temp_in_fahrenheit}")

to_celsius = lambda c:(32 - c) * (5/9)
temp_in_celsius = to_celsius(20)
print(f"Temperature in Celsius is = {temp_in_celsius}")