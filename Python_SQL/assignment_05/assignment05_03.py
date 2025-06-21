# 3) Define a function subtract() that takes two lists and returns difference


def substract():
    list1 = [10, 20, 30, 40]
    list2 = [30, 40, 50, 60]

    result = list(map(lambda n,m:n-m, list2, list1))
    print(f"list = {result}")

substract()