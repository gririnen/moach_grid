
import dot
import random
#import graphicsHandler as gH
import math

# generates a grid with the input side length 
gridSide = int(input("grid side:"))
dot.genGrid(gridSide)
#gH.initGraphics(dot.returnGrid())

dotLs = []
def genMidSquare(side):
	global dotLs
	leftCorn = int((gridSide - side)/2)
	for i in range(side**2):
		dotLs.append(dot.part([int(leftCorn + i/side), leftCorn + i % side]))

def genMidCircle(rad):
	cntr = int(gridSide/2)
	for i in range(gridSide):
		for j in range(gridSide):
			if((i - cntr)**2 + (j - cntr)**2 <=rad**2):
				dotLs.append(dot.part([i, j]))

genMidCircle(4)

#gH.genGraphics(dot.returnGrid())
counter = 0
while not dot.killProgram:
	random.shuffle(dotLs) # important for not creating a bias twords one side
	counter += 1
	for d in dotLs:
		if(dot.killProgram):
			break
		x,y = d.x,d.y
		d.step(dot.genStep())
		#gH.drawStep(x,y,d.x,d.y)
print("steps:", counter)
