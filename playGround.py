import matplotlib.pyplot as plt
import dot
import random
import math
from configFile import config

# generates a grid with the input side length 
if(config["stepsOrReachedEnd"] == "reachedEnd"):
	gridSide = config["gridSideOrSteps"]
elif(config["stepsOrReachedEnd"] == "steps"):
	gridSide = config["gridSideOrSteps"] + config["diameterOrSide"]
else:
	print("bad value in stepsOrReachedEnd")
runs = 1

if("AvgRms" in config["experiments"]):
	runs = int(input("How many runs: "))
lastRmsSum = 0

RmsGraph = False
if("RmsGraph" in config["experiments"]):
	RmsGraph = True

def rms():
	squareSum = 0
	cntr = int(gridSide/2)
	for i in dotLs:
		squareSum += (i.x-cntr)**2
		squareSum += (i.y-cntr)**2
	return math.sqrt(squareSum/len(dotLs))

def genMidSquare(side):
	global dotLs
	leftCorn = int((gridSide - side)/2)
	for i in range(side**2):
		dotLs.append(dot.part([int(leftCorn + i/side), leftCorn + i % side]))

def genMidCircle(dim):
	rad = dim/2
	cntr = int(gridSide/2)
	for i in range(gridSide):
		for j in range(gridSide):
			if((i - cntr)**2 + (j - cntr)**2 <=rad**2):
				dotLs.append(dot.part([i, j]))


for i in range(runs):

	dot.genGrid(gridSide)
	rmsLs = []
	dotLs = []

	if(config["startingShape"] == "square"):
		genMidSquare(config["diameterOrSide"])

	elif(config["startingShape"] == "circle"):
		genMidCircle(config["diameterOrSide"])

	else:
		print("unknown shape in config['startingShape']")

	if("graphics" in config["experiments"]):
		import graphicsHandler as gH
		gH.initGraphics(dot.returnGrid())
		gH.genGraphics(dot.returnGrid())

	counter = 0
	dot.killProgram = False
	while not dot.killProgram:
		random.shuffle(dotLs) # important for not creating a bias twords one side
		if(RmsGraph):
			rmsLs.append(rms())
		for d in dotLs:
			if(dot.killProgram):
				break
			if(config["stepsOrReachedEnd"] == "steps" and counter >= config["gridSideOrSteps"]):
				dot.end()
				#print("success: playGround.py killed the program because it ran out of steps.")
				break
			x,y = d.x,d.y
			d.step(dot.genStep())
			if("graphics" in config["experiments"]):
				gH.drawStep(x,y,d.x,d.y)
		counter += 1

	if(RmsGraph and runs == i + 1):
		print("All ", runs, " runs executed successfully, you should now see the RMS graph of the last one.")
		import matplotlib.pyplot as plt
		plt.plot(rmsLs)
		plt.plot([j**0.5 for j in range(int(rmsLs[0]**2), len(rmsLs) + int(rmsLs[0]**2))])
		plt.xlabel('Iterations')
		plt.ylabel('RMS (blue) and Square root of iterations (orange)')
		plt.show()

	lastRmsSum += rms()

print("The average RMS at the end of the experiment is: ", str(lastRmsSum / runs))
