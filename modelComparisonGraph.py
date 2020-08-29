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
	"""avg(float[]) -> float
	"""
	sumArr = np.array([0 for i in range(steps+1)], dtype=np.float)
	for l in ls:
		sumArr = sumArr + l

	return sumArr / len(ls)

RmsLss2 = []
gridSide = steps*2 + config["diameterOrSide"] + 1 # makes the grid too large for any dot to step out of it with the number of steps it has
config["allow2dotsInTheSamePlace"] = False #sets model type
for i in range(runs*2):
	#runs twice the number of runs as we want two results for the same config
	RmsLs = np.array([], dtype=np.float)
 
	dot.genGrid(gridSide) #generates grid.data
	rmsLs = [] #completely resets rmsLs and dotLs at the beggining of each run
	dotLs = []

	if(config["startingShape"] == "square"):
		genMidSquare(config["diameterOrSide"])

	elif(config["startingShape"] == "circle"):
		genMidCircle(config["diameterOrSide"])

	else:
		print("unknown shape in config['startingShape']")

	counter = 0
	dot.killProgram = False
	while not dot.killProgram:
		random.shuffle(dotLs) # important for not creating a bias twords one side
		for d in dotLs:
			if(dot.killProgram):
				break
			if(counter >= steps):
				dot.end()
				#print("success: playGround.py killed the program because it ran out of steps.")
				break
			x,y = d.x,d.y
			d.step(dot.genStep())

		counter += 1
		RmsLs = np.append(RmsLs, rms())
	RmsLss2.append(RmsLs)
	if(runs == i + 1):
		config["allow2dotsInTheSamePlace"] = True
		falseDevTrue = avg(RmsLss2)
		RmsLss2 = []



falseDevTrue /= avg(RmsLss2)

plt.plot(falseDevTrue)
plt.xlabel('Iterations')
plt.ylabel("The average RMS at the end of the experiment, (new model) ÷ (old model)")
plt.show()

