import random

my_choice = ["stone", 'paper', 'scissors']

print('Welcome to Stone, Paper and Scissors game.')
print()

class SPS(object):
    score_u1 = 0
    score_u2 = 0



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
    
    def score_player(self, user1_choice, user2_choice):
        i = 0

        while i < 10:

            #user1 = input('Enter your choice : ').lower()
            #user2 = random.choice(my_choice)

            if user1_choice == user2_choice:
                print('No Score!')

                ### paper

            elif user1_choice == 'paper' and user2_choice == 'stone':
                self.score_u1 += 1
                print('1 score for user One.')

            elif user1_choice == 'paper' and user2_choice == 'scissors':
                self.score_u2 += 1
                print('1 score for user Two.')

                ### stone
            elif user1_choice == 'stone' and user2_choice == 'paper':
                self.score_u2 += 1
                print('1 score for user Two.')

            elif user1_choice == 'stone' and user2_choice == 'scissors':
                self.score_u1 += 1
                print('1 score for user One.')

                ### scissors
            elif user1_choice == 'scissors' and user2_choice == 'stone':
                self.score_u2 += 1
                print('1 score for user Two.')

            elif user1_choice == 'scissors' and user2_choice == 'paper':
                self.score_u1 += 1
                print('1 score for user One.')

            else:
                print("PLEASE ENTER 'STONE' , 'PAPER' OR 'SCISSORS' ")

            i += 1


    if n_player == 1:
        score_player()
        
    elif n_player == 2:
        pass

