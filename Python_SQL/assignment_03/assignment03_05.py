#  Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.
from operator import itemgetter


def overlapping(l1, l2):
    for item in l1:
        if item in l2:
            return True
    return False

l1 = [1,2,5,43,56]
l2 = [43,53,647,745,266]

print(overlapping(l1, l2))