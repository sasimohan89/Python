# list - a sequence of objects; can have diff data types in a single list
li = [1,2,3]
li1 = ['a','b',3,4,True]

# List slicing
amazon_cart = ['pens', 'paper', 'grapes', 'ball']
new_cart = amazon_cart[:] # makes a copy instead 
amazon_cart[0] = 'eraser'
print(amazon_cart)
print(new_cart)

# Matrix
matrix = [
  [1,2,3],
  [2,3,4],
  [3,4,5]
]
print(matrix)
print(matrix[0])
print(matrix[1][2])

# list actions
# append
matrix.append([4,5,6])
print(matrix)

#insert
matrix.insert(0,[0,1,2])
print(matrix)
matrix.extend([555])  # Add iterable to end
print(matrix)
matrix.pop()  # Remove last element
print(matrix[::-1]) # Reverse a list
new_list = matrix.remove([1,2,3])
print(new_list)
matrix.clear()  # Erase all

# Generate a list
print(list(range(0,100)))

# join
text2 = ' '.join(['yo','kim'])
print(text2)

# List unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8]
print (a)
print (b)
print (c)
print (other)
print (d)
