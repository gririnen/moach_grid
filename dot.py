# create end() to kill the program 
import grid
import random


gridSide = 0
allow2dotsInTheSamePlace = False

class part:
	"""docstring for dot"""
	def __init__(self, ls):
		self.x = ls[0]
		self.y = ls[1]
		self.step([0, 0]) # used for updating grid.data

	def step(self, ls):
		x = ls[0]
		y = ls[1]
		if((self.x + x > gridSide or self.x + x < 0) or (self.y + y > gridSide or self.y + y < 0)):
			end()
			return 0

		if(allow2dotsInTheSamePlace or (not grid.data[self.x + x][self.y + y])): # checks that there isn't another point there already
			grid.data[self.x][self.y] = False
			self.x += x
			self.y += y
			grid.data[self.x][self.y] = True


def genGrid(i):
	grid.genGrid(i)
	global gridSide
	gridSide = i

def returnGrid():
	return grid.data

def end():
	print('killed program')

def genStep():
	if (random.randint(0, 1)):
		return [(1 if random.randint(0,1) else (-1)), 0]
	else:
		return [0, (1 if random.randint(0,1) else (-1))]