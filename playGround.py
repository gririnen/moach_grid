import matplotlib.pyplot as plt
import dot
import random
import math
from configFile import config

# generates a grid with the input side length 
if(config["stepsOrReachedEnd"] == "reachedEnd"):
	gridSide = config["gridSideOrSteps"]
elif(config["stepsOrReachedEnd"] == "steps"):
	gridSide = config["gridSideOrSteps"]*2 + config["diameterOrSide"] + 1# makes the grid too large for any dot to step out of it with the number of steps it has
else:
	print("bad value in stepsOrReachedEnd")
runs = 1 #deafult amount of runs

if("AvgRms" in config["experiments"]):
	#since AvgRms is ther only experiment requiring multiple runs, we only input different run values here
	runs = int(input("How many runs: "))
lastRmsLs = [] #list that saves the RMS for every full grid iteration

RmsGraph = False
if("RmsGraph" in config["experiments"]):
	#saves the fact that we use and RmsGraph experiment, prevents us needeing to access configFile every full iteration
	RmsGraph = True

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


for i in range(runs):
	#runs the experiment for multiple times if set
	dot.genGrid(gridSide) #generates grid.data
	rmsLs = [] #completely resets rmsLs and dotLs at the beggining of each run
	dotLs = []
	
	#generates initial particles
	if(config["startingShape"] == "square"):
		genMidSquare(config["diameterOrSide"])

	elif(config["startingShape"] == "circle"):
		genMidCircle(config["diameterOrSide"])

	else:
		print("unknown shape in config['startingShape']")

	if("graphics" in config["experiments"]):
		import graphicsHandler as gH
		gH.initGraphics(dot.returnGrid()) #generates graphic window
		gH.genGraphics(dot.returnGrid()) #draws current window

	counter = 0 #counts how many steps were taken for a single dot
	dot.killProgram = False
	while not dot.killProgram:
		#loops indefienetly until max steps reached or particle reached the end
		random.shuffle(dotLs) # important for not creating a bias twords one side
		if(RmsGraph):
			rmsLs.append(rms()) #appends current rms to the list to be used in the graph
		for d in dotLs:
			#loops for every dot
			
			if(dot.killProgram):
				break #if killstate was reached in the middle of the run this will stop the loop
			if(config["stepsOrReachedEnd"] == "steps" and counter >= config["gridSideOrSteps"]):
				dot.end() #kills program if max number of steps was reached in steps experiment
				#print("success: playGround.py killed the program because it ran out of steps.") (testing)
				break
			
			x,y = d.x,d.y
			d.step(dot.genStep()) #particle takes a step
			
			if("graphics" in config["experiments"]):
				gH.drawStep(x,y,d.x,d.y) #draws the new step
		counter += 1

	if(RmsGraph and runs == i + 1):
		#plots gaph of RMS by runs
		print("You should now see the RMS graph of the last run.")
		import matplotlib.pyplot as plt
		plt.plot(rmsLs)
		plt.plot([j**0.5 for j in range(int(rmsLs[0]**2), len(rmsLs) + int(rmsLs[0]**2))]) #plots graph of sqrt(x)
		plt.xlabel('Iterations')
		plt.ylabel('RMS (blue) and Square root of iterations (orange)')
		plt.show()

	lastRmsLs.append(rms())

if(runs > 1):
	import numpy
	print("The average RMS at the end of the experiment, of all the ", runs," runs is: ", str(sum(lastRmsLs) / runs)) #prints avarage RMS of the last grid state
	print("The standard deviation is: ", numpy.std(lastRmsLs)) #prints standard deviation of the last grid state

else:
	print("The RMS at the end of the experiment was: ", str(lastRmsLs[0])) #prints RMS of the last grid state
