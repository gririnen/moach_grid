
import dot
import random
import math
from configFile import config

# generates a grid with the input side length 
gridSide = config["gridSide"]
dot.genGrid(gridSide)


dotLs = []
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

def genDot(n):
	cntr = int(gridSide/2)
	for i in range(n):
		dotLs.append(dot.part([cntr, cntr]))

if(config["startingShape"] == "square"):
	genMidSquare(config["diameterSideOrNumberOfDots"])

elif(config["startingShape"] == "circle"):
	genMidCircle(config["diameterSideOrNumberOfDots"])

elif(config["startingShape"] == "dot"):
	genDot(config["diameterSideOrNumberOfDots"])

else:
	print("unknown shape in config['startingShape']")

if(config["graphics"]):
	import graphicsHandler as gH
	gH.initGraphics(dot.returnGrid())
	gH.genGraphics(dot.returnGrid())

counter = 0
while not dot.killProgram:
	random.shuffle(dotLs) # important for not creating a bias twords one side
	counter += 1
	for d in dotLs:
		if(dot.killProgram):
			break
		x,y = d.x,d.y
		d.step(dot.genStep())
		if(config["graphics"]):
			gH.drawStep(x,y,d.x,d.y)
print("steps:", counter)
