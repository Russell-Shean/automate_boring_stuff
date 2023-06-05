# rock_paper_python.py

import random
import time
import sys

from plotly.graph_objs import Bar, Layout
from plotly import offline

n_wins = 0
n_losses = 0
n_ties = 0
possible_moves = ["ROCK", "PAPER", "SCISSORS"]

print("\nRock, Paper, Scissors\n___A Python Game___\n")
print(f"{n_wins} Wins, {n_losses} Losses, {n_ties} Ties")

while True:
	
	player_move = input("Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit\n")

	if player_move == "q":
		break

	if player_move == "r":
		player_move = "ROCK"

	elif player_move == "p":
		player_move = "PAPER"

	elif player_move == "s":
		player_move = "SCISSORS"

	computer_move = random.sample(possible_moves, 1)[0]


	# tie ---------------------------------------------------


	if player_move == computer_move:
		outcome = "It's a Tie!"
		n_ties = n_ties + 1

	# player wins -------------------------------------------

	elif player_move == "ROCK" and computer_move == "SCISSORS":
		outcome = "You win!"
		n_wins = n_wins + 1

	elif player_move == "PAPER" and computer_move == "ROCK":
		outcome = "You win!"
		n_wins = n_wins + 1

	elif player_move == "SCISSORS" and computer_move == "PAPER":
		outcome = "You win!"
		n_wins = n_wins + 1


	# computer wins -----------------------------------------

	elif computer_move == "ROCK" and player_move == "SCISSORS":
		outcome = "You lose  QQ"
		n_losses = n_losses + 1

	elif computer_move == "PAPER" and player_move == "ROCK":
		outcome = "You lose  QQ"
		n_losses = n_losses + 1

	elif computer_move == "SCISSORS" and player_move == "PAPER":
		outcome = "You lose  QQ"
		n_losses = n_losses + 1



	print(f"{player_move} versus...")
	time.sleep(2)
	print(f"{computer_move}\n{outcome}")
	print(f"{n_wins} Wins, {n_losses} Losses, {n_ties} Ties")

		


print("Thanks for playing!")
see_stats = input("See stats? (y/n) ")

if see_stats == "n":
	sys.exit()

elif see_stats == "y":
	frequencies = [n_wins, n_losses, n_ties]
	outcomes = ["Wins", "Losses", "Ties"]


	labels = []

	for i in range(len(frequencies)):

		if sum(frequencies) == 0:
			label = "0 out of 0"

		else:
			label = f"{frequencies[i]} out of {sum(frequencies)} games <br> {round((frequencies[i] / sum(frequencies) * 100), 2)}%"
		
		labels.append(label)


	data = [{
	         'type':'bar',
	         'x': outcomes,
	         'y': frequencies,
	         'hovertext': labels,
	         'marker': {
	                    'color': 'purple',
	                    'line' : {'width': 5, 'color': 'green'},
	                    'opacity': 0.85

	         }
	}]

	chart_layout = {
	          'title': "Your game Stats",
	          'titlefont': {'color':'purple', 'size': 35},
	          'xaxis': { 'title': 'Outcome',
	           'titlefont':{'size': 24},
	           'tickfont': {'size': 14, 'color': "green"}},
	'yaxis': { 'title': 'frequency',
	           'titlefont': {'size':24},
	           'tickfont': {'size': 14}}

	}


	fig = {'data': data, 'layout': chart_layout}

	offline.plot(fig, filename = "rock_paper_python_stats.html")





