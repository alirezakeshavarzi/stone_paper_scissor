import random

my_choice = ["stone", 'paper', 'scissors']

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

        break
    else:
        print()
        print('Just enter 1 or 2.')
        print()



### add condition

def score_player(user1_choice, user2_choice):
    i = 0

    score_u1 = 0
    score_u2 = 0

    while i < 10:



        if user1_choice == user2_choice:
            print('No Score!')

            ### paper

        elif user1_choice == 'paper' and user2_choice == 'stone':
            score_u1 += 1
            print('1 score for user One.')

        elif user1_choice == 'paper' and user2_choice == 'scissors':
            score_u2 += 1
            print('1 score for user Two.')

            ### stone
        elif user1_choice == 'stone' and user2_choice == 'paper':
            score_u2 += 1
            print('1 score for user Two.')

        elif user1_choice == 'stone' and user2_choice == 'scissors':
            score_u1 += 1
            print('1 score for user One.')

            ### scissors
        elif user1_choice == 'scissors' and user2_choice == 'stone':
            score_u2 += 1
            print('1 score for user Two.')

        elif user1_choice == 'scissors' and user2_choice == 'paper':
            score_u1 += 1
            print('1 score for user One.')

        else:
            print("PLEASE ENTER 'STONE' , 'PAPER' OR 'SCISSORS' ")

        i += 1

        ### winner player
        if score_u1 > score_u2:
            print('player 1 win')
        elif score_u1 < score_u2:
            print('player 2 win')
        else:
            print('equ.')


if n_player == 1:

    user1 = input('Enter your choice : ').lower()
    user2 = random.choice(my_choice)
    score_player(user1, user2)

elif n_player == 2:
    user1 = input('Player1 , Enter your choice : ').lower()
    user2 = input('Player2 , Enter your choice : ').lower()
    score_player(user1, user2)


#s = SPS()