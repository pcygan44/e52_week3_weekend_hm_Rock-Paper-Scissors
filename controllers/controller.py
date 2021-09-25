from flask import render_template, request, redirect
from app import app 
from models.player import Player
from models.game import *
from models.players import  players


# @app.route("/players")
# def index():
#     return render_template("index.html", title = "home" , players = players )


@app.route("/<choice1>/<choice2>")

def game_resolt(choice1, choice2):
    

    player1 = Player("player1",choice1)
    player2 = Player("player2", choice2)
    answer = game(player1, player2)

    return render_template("index.html", title = "Home" ,answer = answer)

