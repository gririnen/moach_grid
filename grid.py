data = [] #two dimentional list that saves the locations of the particles for easy access
def genGrid(gridSide):
	"""genGrid(int) -> void
	makes the data grid gridSide long on both dimentions. data must be empty"""
	for i in range(gridSide):
		temp = []
		for j in range(gridSide):
	  		temp.append(0)
		data.append(temp)
