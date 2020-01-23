# Tuples - Immutable lists
my_tuple = (1,2,3,4,5)
print(my_tuple[2])
new_tuple = my_tuple[2:4] # slice tuple
print(new_tuple)
x,y,z, *other = my_tuple
print(other)

# Sets - unordered collections of unique objects
my_set = {1,2,3,4,5,5}
print(my_set)
list1 = [1,2,3,4,5,5]
set1 = set(list1) # Convert list to Set - eliminate duplicates!
print(set1) # Set object does not support indexing; set1[0] = error

# Set methods
set2 = {1,2,3,4,5}
set3 = {4,5,6,7,8,9,10}

# print(set2.difference(set3))
# print(set2.discard(5))
# print(set2)
# print(set2.difference_update(set3))
# print(set2)
# print(set2.intersection(set3))
print(set2.isdisjoint(set3))
print(set2 | set3)