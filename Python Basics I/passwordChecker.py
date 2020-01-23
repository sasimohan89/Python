# password checker program
username = input('username: ')
password = input('password: ')
password_length = len(password)
hidden_password = '*' * password_length
print(username + ', your password ' + hidden_password + ' is ' + 
str(password_length) + ' letters long')
  
print(f'{username}, your password {hidden_password} is {password_length} letters long')