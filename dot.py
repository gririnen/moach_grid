# create end() to kill the program 

class part:
	"""docstring for dot"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def step(x, y):
		if(self.x + x > gridSide or self.y + y > gridSide):
#			end()
			return 0;

		if(not grid[self.x + x][self.y + y]):
			grid[self.x][self.y] = False
			self.x += x
			self.y += y
			grid[self.x][self.y] = True
