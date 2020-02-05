# is_magician = False
# is_expert = True

# if is_expert and is_magician:
#   print("you are a master magician") 

# if is_magician and not is_expert:
#   print('at least you\'re getting there')

# if not is_magician:
#   print('you need magic powers')

# Loops
# for x in 'abcdefgh':
#   print(x)

dictionary = {
  'a': [1,2,3],
  'b': True,
  'c': 'Hi'
}

for key, value in dictionary.items():
  print(key, value) # Tuple can be split and printed with multiple variables in iteration

for item in dictionary.keys():
  print(item)

for item in dictionary.values():
  print(item)