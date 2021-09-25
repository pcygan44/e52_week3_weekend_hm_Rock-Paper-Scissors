from models.player import Player
from models.players import players

def game( player1, player2):
    if player1.choice == "rock" and player2.choice == "rock":
        return(None)
    
    elif player1.choice == "paper" and player2.choice == "paper":
        return(None)

    elif player1.choice == "scissors" and player2.choice == "scissors":
        return(None)

    elif player1.choice == "scissors" and player2.choice == "paper":
        return("Player1 wins with scissors")

    elif player1.choice == "paper" and player2.choice == "rock":
        return("Player1 wins with paper")

    elif player1.choice == "rock" and player2.choice == "scissors":
        return("Player1 wins with rock")

    elif player1.choice == "rock" and player2.choice == "paper":
        return("Player2 wins with paper")

    elif player1.choice == "paper" and player2.choice == "scissors":
        print("Player2 wins with scissors")

    elif player1.choice == "scissors" and player2.choice == "rock":
        print("Player2 wins with rock")