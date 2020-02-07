# Functions

# parameters
# def say_hello(name, emoji):
#   print(f'hellooo {name}, welcome {emoji}')

# # arguments
# say_hello('John', ':P')
# say_hello('Brian', ':P')

# return

def sum(num1, num2):
  def another_func(n1, n2):
    return n1 + n2
  return num1 + num2  # return ends the command/control within a                            function

total = sum(10, 20)
print(total)
