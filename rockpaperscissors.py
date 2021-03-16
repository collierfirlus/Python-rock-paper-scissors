import random

random.seed()

def start():
    wins, losses, ties = 0, 0, 0
    while True:
        
        p_move = input("Rock, paper, or scissors?: ")

        moves = ["rock", "paper", "scissors"]
        move = random.choice(moves)

        print("You chose: ", p_move, " Opponent chose: ", move)

        if move == p_move:
            print("Tie!")
            ties += 1
        elif move == "rock":
            if p_move == "paper":
                print("You win!")
                wins += 1
            else:
                print("You lose.")
                losses += 1
        elif move == "paper":
            if p_move == "scissors":
                print("You win!")
                wins += 1
            else:
                print("You lose.")
                losses += 1
        else:
            if p_move == "rock":
                print("You win!")
                wins += 1
            else:
                print("You lose.")
                losses += 1

        print("Wins: ", wins, "Losses: ", losses, " Ties: ", ties)

        choice = input("Play again? (Y/N): ")
        if choice.lower() == 'y':
            print("Playing again...")
        else:
            break
start()