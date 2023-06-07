#conway.py

# conway's game of life

import random
import time
import copy

width = 60
height = 20

# create a list of lists for the cells
rows = []

for x in range(width):
	# create a new column:
	column = []

	for y in range(height):
		if random.randint(0,1) == 0:
			column.append("#") # add a living cell

		else:
			column.append(" ") # add a dead cell

	rows.append(column)


for y in range(height):
	for x in range(width):
		print(rows[x][y], end = "")
	print()