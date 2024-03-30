import random
ROCK = 1
PAPER = 2
SCISSORS = 3

PLAYER_WINS = "Player wins!! Woop woop!"
COMPUTER_WINS = "Robocop wins :-("
TIE = "It's a tie!"

player=()
comp=()

def rps(player, comp):
    print("Welcome to play rock-paper-scissors")
    print("The options are:\nrock: 1\npaper: 2\nscissors: 3")
    player = int(input('vvodi: '))
    print('vibor igroka:', end=" ")
    if player == ROCK:
        print("rock")
    elif player == PAPER:
        print("paper")
    elif player == SCISSORS:
        print("scissors")
    comp = random.randint(1,3)
    print('vibor compa:', end=" ")
    if comp == ROCK:
        print("rock")
    elif comp == PAPER:
        print("paper")
    elif comp == SCISSORS:
        print("scissors")
    if not player in [1, 2, 3]:
        print("Invalid choice")
    elif player==ROCK:
        if comp==ROCK:
            return TIE
        elif comp==PAPER:
            return COMPUTER_WINS
        elif comp==SCISSORS:
            return PLAYER_WINS
    elif player == PAPER:
        if comp==PAPER:
            return TIE
        elif comp==SCISSORS:
            return COMPUTER_WINS
        elif comp==ROCK:
            return PLAYER_WINS
    elif player == SCISSORS:
        if comp==SCISSORS:
            return TIE
        elif comp==ROCK:
            return COMPUTER_WINS
        elif comp==PAPER:
            return PLAYER_WINS

print(rps(player,comp))