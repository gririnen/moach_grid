import grid
import random
from configFile import config


killProgram = False
gridSide = 0 #is set a different value in genGrid

class part:
	"""part class, saves x and y values"""
	def __init__(self, ls):
		"""__init__([int, int]) -> part
		sets part x and y values to those in list"""
		self.x = ls[0]
		self.y = ls[1]
		self.step([0, 0]) # used to update grid.data and not for actually stepping, steps 0 in each direction

	def step(self, ls):
		"""step([int, int]) -> void (wil return 0 to kill program under certain requirements)
		makes the part do a step and updates grid.data.
		adds x and y from list to part's current x, y"""
		x = ls[0]
		y = ls[1] #saves the direction the dot will try to step
		if((self.x + x >= gridSide or self.x + x < 0) or (self.y + y >= gridSide or self.y + y < 0)):
			end() #if dot is out of grid boundaries ends program, evades list index out of range error
			return 0

		if(config["allow2dotsInTheSamePlace"] or (grid.data[self.x + x][self.y + y]) != 1): # checks that there isn't another part there already,and the run's config file
			grid.data[self.x][self.y] = 2 # saves part's old position as 2 in grid.data, for colorSteppedPlaces config option
			self.x += x
			self.y += y #updates the part's position
			grid.data[self.x][self.y] = 1 #updates grid.data with current part coordinations


def genGrid(i):
	"""genGrid(int) -> void
	initializes grid.data with size of int"""
	grid.genGrid(i) #generates grid.data as grid with i long sides
	global gridSide
	gridSide = i #sets gridSide as i

def returnGrid():
	"""returnGrid() -> int[][]
	returns grid.data"""
	return grid.data

def end():
	"""end() -> void
	sets killProgram to true, can be read to stop program in loops. also resets grid.data"""
	global killProgram
	killProgram = True
	grid.data = [] #reset grid.data

def genStep():
	"""genStep() -> [int,int]
	returns list with x,y values of step, one out of four directions at random"""
	if (random.randint(0, 1)): #if 0 the part moves on y axis, if 1 the part moves on the y axis
		return [(1 if random.randint(0,1) else (-1)), 0] #if 0 the part moves to the negative direction, positive if 1
	else:
		return [0, (1 if random.randint(0,1) else (-1))] #if 0 the part moves to the negative direction, positive if 1


