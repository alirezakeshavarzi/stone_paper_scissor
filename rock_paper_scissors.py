import random

my_choice = ["Stone", 'Paper', 'Scissors']

print('Welcome to Stone, Paper and Scissors game.')
print()

### Add description and select choice

while (1):
    print('Choose the number of players.')
    print('1. One player')
    print('2. Two player')

    print('Choose one of the options : ')
    n_player = int(input())

    if n_player == 1 or n_player == 2:
        print()
        print('Just enter 1 or 2.')
        print()
        break



### add condition
if n_player == 1:
    pass
elif n_player == 2:
    pass

user1 = input('Enter your choice : ')
user2 = ran