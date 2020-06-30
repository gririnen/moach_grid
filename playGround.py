import dot
import random
import graphicsHandler as gH

# generates a grid with the input side length 
gridSide = int(input("grid side:"))
dot.genGrid(gridSide)
gH.initGraphics(dot.returnGrid())

dotLs = []
def genMidSquare(side):
	global dotLs
	leftCorn = int((gridSide - side)/2)
	for i in range(side**2):
		dotLs.append(dot.part([int(leftCorn + i/side), leftCorn + i % side]))

genMidSquare(10)

gH.genGraphics(dot.returnGrid())
counter = 0
while dot.killProgram == False:
	counter += 1
	random.shuffle(dotLs) # important for not creating a bias twords one side
	for d in dotLs:
		x,y = d.x,d.y
		d.step(dot.genStep())
		gH.drawStep(x,y,d.x,d.y)
	#gH.genGraphics(dot.returnGrid())