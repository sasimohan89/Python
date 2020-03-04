# Map, filter, zip and reduce
from functools import reduce
my_list = [2, 3, 5, 6, 7]
your_list = [20, 30, 50, 60]
def multiply_by_2(item):
    return item*2

def check_even(item):
    return item % 2 == 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(list(map(multiply_by_2, [2, 3])))     # map(action, data) - returns map object
print(list(filter(check_even, my_list)))     # filter(action, data) - returns map object
print(list(zip(my_list, your_list)))        # creates tuples
print(my_list)  # not modified
print(reduce(accumulator, my_list, 10))