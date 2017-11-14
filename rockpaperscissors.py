from random import randint

def output_winner (computer_score, user_score):
    if computer_score < user_score:
        print('Congratulations, you won this round!')
    elif computer_score > user_score:
        print('Sorry, this time you lost this round!')
    elif computer_score == user_score:
        print('Nobody won this round!')

current_round = 1
tries = 3
computer_won = 0
user_won = 0

while current_round <= tries:
    try:
        user = int(input("What are you? (1 = Scissors, 2 = Rock, 3 = Paper)"))
    except ValueError:
        print("Please enter a valid value!")
    else:
        computer = randint(1, 3)
        if (computer == user):
            print("Tie!")
        elif ((computer == 1 and user == 2) or (computer == 2 and user == 3) or (computer == 3 and user == 1)):
            computer_won += 1
            print('Sorry, you lost!')
        elif ((computer == 1 and user == 3) or (computer == 2 and user == 1) or (computer == 3 and user == 2)):
            user_won += 1
            print('You won!')
        print('Computer was ' + str(computer))
        current_round += 1;

output_winner(computer_won, user_won)