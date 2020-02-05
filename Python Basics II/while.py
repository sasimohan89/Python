# # Counter
# my_list = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in my_list:
#   sum = sum + i 
# print(sum)

# # Range
# for _ in range(50,0,-3):
#   print(_)

# for i in range(10):
#   print(list(range(0,10)))

# for i, char in enumerate(list(range(100))):
#   if char == 50: 
#     print(f'The index of 50 is {i}')
# print(list(range(0, 50, 2)))

my_list = [1,2,3]

i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1

for item in my_list:
  continue  # passes control to beginning of loop
  print(item)

