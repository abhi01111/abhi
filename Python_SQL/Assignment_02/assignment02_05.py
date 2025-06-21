"""Write a program that prompts the user to input number of calls and calculate the monthly
telephone bills
as per the following rule:
Minimum Rs. 200 for up to 100 calls.
Plus Rs. 0.60 per call for next 50 calls.
Plus Rs. 0.50 per call for next 50 calls.
Plus Rs. 0.40 per call for any call beyond 200 calls."""

calls = int(input("Number of Calls in Month : "))

def bill():
    if calls >100 and calls < 150:
        print(f"your bill is {(calls - 100) * 0.60 + 200}")
    elif calls > 150 and calls < 200:
        print(f" your bill is {(calls - 150) * 0.50 + 200}")
    elif calls > 200:
        print(f" your bill is {(calls - 100) * 0.40 + 200} ")
    else:
        print(f"Dont pay its fraud")

bill()