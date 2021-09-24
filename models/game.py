from player import Players
from players import players

def game(self, player1, player2):
    if player1.choice == "rock" and player2.choice == "rock":
        print(None)
    
    elif player1.choice == "paper" and player2.choice == "paper":
        print(None)

    elif player1.choice == "scissors" and player2.choice == "scissors":
        print(None)

    elif player1.choice == "scissors" and player2.choice == "paper":
        print("Player1 wins with scissors")

    elif player1.choice == "paper" and player2.choice == "rock":
        print("Player1 wins with paper")

    elif player1.choice == "rock" and player2.choice == "scissors":
        print("Player1 wins with rock")

    elif player1.choice == "rock" and player2.choice == "paper":
        print("Player2 wins with paper")

    elif player1.choice == "paper" and player2.choice == "scissors":
        print("Player2 wins with scissors")

    elif player1.choice == "scissors" and player2.choice == "rock":
        print("Player2 wins with rock")