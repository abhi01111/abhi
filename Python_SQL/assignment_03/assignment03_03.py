# Replace single element ‘b’ in given list[’a’, ’b’, ’c’, ’d’, ’e’] with [1, 2, 3].
from operator import index

list = ['a' , 'b' , 'c' , 'd' , 'e']
print(f"list {list}")
index = list.index('b')
list[index:index + 1] = [1,2,3]

print(f"List = {list}")