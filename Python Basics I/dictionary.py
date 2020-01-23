# Dictionary
dictionary = {
  'a': [1,2,3],
  'b': True,
  'c': 'Hi'
}
print(dictionary)
print(dictionary['a'][2])

my_list = [
  {
  'a': [1,2,3],
  'b': True,
  'c': 'Hi'
  },
  {
  'x': [4,2,3],
  'y': False,
  'z': 'Bye'
  }
]
print(my_list)
print(my_list[0]['a'])
print(my_list[0])
print(my_list[0]['a'][0])

# Dictionary keys are immutable - Mostly strings

# Dictionary methods
user = {
  'basket': [1,2,3],
  'greet': 'hello',
  'age': 20
}
print(user.get('age',55))
print(user)
user1 = dict(name='SyntaxWarning')
print(user1)
print('basket' in user.keys())
print(user.items())
print(user.keys())