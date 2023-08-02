'''a = 2
def sum():
    global a
    a = a+2
sum()
print(a)'''

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


#global score_u1,score_u2


### add condition

def score_player(n_player):
    user1_choice = user2_choice = ""
    global score_u1, score_u2

    score_u1 = score_u2 = 0

    i = 0
    while i < 3:
        if n_player == 1:
            user1_choice = input('Player1, Enter your choice : ').lower()
            user2_choice = random.choice(my_choice)

            print('Player1, your choice : ', user1_choice)
            print('Player2, your choice : ', user2_choice)

        elif n_player == 2:
            user1_choice = input('Player1, Enter your choice : ').lower()
            user2_choice = input('Player2, Enter your choice : ').lower()



        if user1_choice == user2_choice:
            print('score user1 : {0}\nscore user2 : {1}' .format(score_u1, score_u2))
            print()

            ### paper

        elif user1_choice == 'paper' and user2_choice == 'stone':
            score_u1 += 1
            print('score user1 : {0}\nscore user2 : {1}' .format(score_u1, score_u2))
            print()

        elif user1_choice == 'paper' and user2_choice == 'scissors':
            score_u2 += 1
            print('score user1 : {0}\nscore user2 : {1}' .format(score_u1, score_u2))
            print()

            ### stone
        elif user1_choice == 'stone' and user2_choice == 'paper':
            score_u2 += 1
            print('score user1 : {0}\nscore user2 : {1}' .format(score_u1, score_u2))
            print()

        elif user1_choice == 'stone' and user2_choice == 'scissors':
            score_u1 += 1
            print('score user1 : {0}\nscore user2 : {1}' .format(score_u1, score_u2))
            print()

            ### scissors
        elif user1_choice == 'scissors' and user2_choice == 'stone':
            score_u2 += 1
            print('score user1 : {0}\nscore user2 : {1}' .format(score_u1, score_u2))
            print()

        elif user1_choice == 'scissors' and user2_choice == 'paper':
            score_u1 += 1
            print('score user1 : {0}\nscore user2 : {1}' .format(score_u1, score_u2))
            print()

        else:
            print("PLEASE ENTER 'STONE' , 'PAPER' OR 'SCISSORS' ")
            i -= 1
            print()

        i += 1

    if score_u1 > score_u2:
        print('user 1 win')
    elif score_u1 < score_u2:
        print('user 2 win')
    else:
        print('equ.')




### end of function


def main(n_player):
    score_u1 = 0
    score_u2 = 0

    print('before while : score u1 : {0} , score u2 : {1} '.format(score_u1, score_u2))
    score_player(n_player)
    print()



        ### winner player






# main

if n_player == 1:
    main(n_player)
elif n_player == 2:
    main(n_player)

#s = SPS()