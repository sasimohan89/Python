# Find duplicates and print em

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# set1 = set()
# for letter in some_list:  
#   if letter in set1:
#     print(letter)
#   set1.add(letter)

i = 0
another_list = []
duplicates_list = []
while i < len(some_list):
  if some_list[i] in another_list:
    duplicates_list.append(some_list[i])
  else:
    another_list.append(some_list[i])
  i += 1
print(duplicates_list)