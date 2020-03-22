import sys
from random import randint

# sys.argv()
rnd_numb = randint(sys.argv[1], sys.argv[2])    # input taken in terminal along with file name

while True:
    try:
        number = input(print(f'Enter a number between {sys.argv[1]} and {sys.argv[2]}: '))
        if 0 < int(number) < 11:
            if int(rnd_numb) == number:
                print(f'Guessed it right! {number}')
                break
        else:
            print('Hey! Enter number only between 1 and 10')
    except ValueError:
        print('Enter only number!')