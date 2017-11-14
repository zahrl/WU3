from random import randint

class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass

def output_round_winner (computer_score, user_score):
    if computer_score < user_score:
        print('Congratulations, you won this round!')
    elif computer_score > user_score:
        print('Sorry, this time you lost this round!')
    elif computer_score == user_score:
        print('Nobody won this round!')

def compute_result (computer, user):
    if computer == user:
        return -1
    elif ((computer == 1 and user == 2) or (computer == 2 and user == 3) or (computer == 3 and user == 1)):
        return 1
    elif ((computer == 1 and user == 3) or (computer == 2 and user == 1) or (computer == 3 and user == 2)):
        return 0

current_try = 1
tries = 3
computer_won = 0
user_won = 0

while current_try <= tries:
    try:
        user = int(input("What are you? (1 = Scissors, 2 = Rock, 3 = Paper)"))
        if user < 1:
            raise ValueTooSmallError
        elif user > 3:
            raise ValueTooLargeError
    except TypeError:
        print("Please enter a valid value!")
    except ValueTooSmallError:
        print("The value is too small!")
    except ValueTooLargeError:
        print("The value is too large!")
    else:
        computer = randint(1, 3)

        if (computer == user):
            assert(compute_result(computer, user)) ==  -1
            print("Tie!")
        elif ((computer == 1 and user == 2) or (computer == 2 and user == 3) or (computer == 3 and user == 1)):
            assert(compute_result(computer, user)) ==  1
            user_won += 1
            print('You won!')
        elif ((computer == 1 and user == 3) or (computer == 2 and user == 1) or (computer == 3 and user == 2)):
            assert(compute_result(computer, user)) ==  0
            computer_won += 1
            print('Sorry, you lost!')
            
        print('Computer was ' + str(computer))
        current_try += 1;

output_round_winner(computer_won, user_won)