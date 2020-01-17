# password checker program
username = input('username: ')
password = input('password: ')
passwordLength = len(password)
print("{username}, your password {'*' * passwordLength} is {passwordLength} long")