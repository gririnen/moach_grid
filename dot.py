# create end() to kill the program 
import grid
import random
from configFile import config


killProgram = False
gridSide = 0

class part:
	"""docstring for dot"""
	def __init__(self, ls):
		self.x = ls[0]
		self.y = ls[1]
		self.step([0, 0]) # used to update grid.data and not for actually stepping

	def step(self, ls):
		x = ls[0]
		y = ls[1]
		if((self.x + x >= gridSide or self.x + x < 0) or (self.y + y >= gridSide or self.y + y < 0)):
			end()
			return 0

		if(config["allow2dotsInTheSamePlace"] or (grid.data[self.x + x][self.y + y]) != 1): # checks that there isn't another point there already
			grid.data[self.x][self.y] = 2 # 0 is empty 1 has a dot on in 2 had a dot on it
			self.x += x
			self.y += y
			grid.data[self.x][self.y] = 1


def genGrid(i):
	grid.genGrid(i)
	global gridSide
	gridSide = i

def returnGrid():
	return grid.data

def end():
	global killProgram
	killProgram = True
	grid.data = []

def genStep():
	if (random.randint(0, 1)):
		return [(1 if random.randint(0,1) else (-1)), 0]
	else:
		return [0, (1 if random.randint(0,1) else (-1))]


