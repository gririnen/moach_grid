# create end() to kill the program 
import grid

gridSide = 0


class part:
	"""docstring for dot"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.step(0, 0) # used for updating grid.data

	def step(self, x, y):
		if(self.x + x > gridSide or self.y + y > gridSide):
#			end()
			return 0

		if(not grid.data[self.x + x][self.y + y]): # checks that there isn't another point there already
			grid.data[self.x][self.y] = False
			self.x += x
			self.y += y
			grid.data[self.x][self.y] = True


def genGrid(i):
	grid.genGrid(i)
	global gridSide
	gridSide = i

def printGrid():
	print(grid.data)