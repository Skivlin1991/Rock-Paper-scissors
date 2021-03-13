from flask import Flask
from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/rps/<player1answer>/<player2answer>')
def game(player1answer,player2answer):
    if is_a_tie(player1answer,player2answer):
        winner_name = "it a tie"
    elif is_player1_winner(player1answer,player2answer):
        winner_name = "player1"
    else:
        winner_name = 'player2'
    return render_template('game.html',winner_name= winner_name)
    
def is_a_tie(player1answer,player2answer):
    return player1answer == player2answer  
def is_player1_winner(player1answer,player2answer):
    if player1answer == "rock":
        return player2answer =="scissors"
    elif player1answer == "paper":
        return player2answer =="rock"
    elif player1answer== "scissors":
        return player2answer == "paper"

        # @app.route('/login', methods=['GET', 'POST'])
        # def login():
        #     error = None
        #     if request.method == 'POST':
        #         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
        #             error = 'Invalid Credentials. Please try again.'
        #         else:
        #             return redirect(url_for('home'))
        #     return render_template('login.html', error=error)