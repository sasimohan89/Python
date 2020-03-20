# Comprehensions - Lists, sets and dictionaries

# list1 = []
# for char in 'hello':
#     list1.append(char)

my_list = {char for char in 'hello'}
my_list1 = [num for num in range(0,100)]
my_list2 = [num*2 for num in range(0,100)]
my_list3 = [num**2 for num in range(0,100) if num%2 == 0]

print(my_list)

dict1 = {
    'a': 1,
    'b': 2
}

my_dict = {k:v**2 for k,v in dict1.items()
           if v%2==0}
print(my_dict)

some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)