import matplotlib.pyplot as plt
import dot
import random
import math
import matplotlib.pyplot as plt
from configFile import config
import numpy as np

#since modelComparisonGraph is only AvgRms testing, there's no need to identify experiment in configFile
steps = int(input("What's the maximum number of steps you want to see: "))
runs = int(input("How many runs: "))

falseDevTrue = []

def rms():
	"""rms() -> float
	returns rms for current grid using dotLs"""
	squareSum = 0
	cntr = int(gridSide/2) #center of grid
	for i in dotLs:
		squareSum += (i.x-cntr)**2
		squareSum += (i.y-cntr)**2
	return math.sqrt(squareSum/len(dotLs)) #calculates RMS

def genMidSquare(side):
	"""genMidSquare(int) -> void
	generates a sqaure in the middle of the grid full of parts"""
	global dotLs
	leftCorn = int((gridSide - side)/2)
	for i in range(side**2):
		dotLs.append(dot.part([int(leftCorn + i/side), leftCorn + i % side])) #appends particle to dotLs

def genMidCircle(dim):
	"""genMidSquare(int) -> void
	generates a circle in the middle of the grid full of parts"""
	rad = dim/2
	cntr = int(gridSide/2)
	for i in range(gridSide):
		for j in range(gridSide):
			if((i - cntr)**2 + (j - cntr)**2 <=rad**2): #checks if particle is inside the circle with given diameter
				dotLs.append(dot.part([i, j])) #appends particle to dotLs
def avg(ls):
	"""avg(list) -> numpy array
	ls is a list containing numpy arrays with the same lengths filled with floats, avg(ls) returns a numpy array so that avg(ls)[n] is the average value of all the floats contained in the n-th elements of the arrays containd in ls.
	"""
	sumArr = np.array([0 for i in range(steps+1)], dtype=np.float)
	for l in ls:
		sumArr = sumArr + l

	return sumArr / len(ls)

RmsLss2 = [] # going to contain the numpy arrays containing the RMS values
gridSide = steps*2 + config["diameterOrSide"] + 1 # makes the grid too large for any dot to step out of it with the number of steps it has
config["allow2dotsInTheSamePlace"] = False #sets model type
for i in range(runs*2):
	#loops through twice the number of inputted runs, as we want to loop through runs iterations for each model type 
	RmsLs = np.array([], dtype=np.float) #a numpy array that's going to contain the RMS values for the run
 
	dot.genGrid(gridSide) #generates grid.data
	dotLs = []
	
	# creates the starting shape
	if(config["startingShape"] == "square"): 
		genMidSquare(config["diameterOrSide"])

	elif(config["startingShape"] == "circle"):
		genMidCircle(config["diameterOrSide"])

	else:
		print("unknown shape in config['startingShape']")

	
	counter = 0
	dot.killProgram = False
	while not dot.killProgram: #loops indefienetly until max steps reached or particle reached the end (not supposed to happen in this case but is still here to avoid err)
		random.shuffle(dotLs) # important for not creating a bias twords one side
		for d in dotLs:
			#loops for every particle
			if(dot.killProgram):
				break
			if(counter >= steps):
				dot.end() #kills program if max number of steps was reached
				break
			d.step(dot.genStep()) #particle takes a step

		counter += 1
		RmsLs = np.append(RmsLs, rms()) # adds the current RMS to Rmsls
	RmsLss2.append(RmsLs)
	if(runs == i + 1): # when half the iterations already executed (after runs iterations):
		config["allow2dotsInTheSamePlace"] = True # switch to the standart model
		falseDevTrue = avg(RmsLss2) # feed falseDevTrue with the average RMS numpy array for the alternative model
		RmsLss2 = [] # clear RmsLss2 so that data for the standart model can come in instead of data for the alternative model



falseDevTrue /= avg(RmsLss2) # calculates the proportion between the average RMS of the alternative model to the average RMS of the standart model

# plots the graph
plt.plot(falseDevTrue)
plt.xlabel('Iterations')
plt.ylabel("The average RMS at the end of the experiment, (new model) ÷ (old model)")
plt.show()

