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

genMidSquare(3)

while True:
	gH.genGraphics(dot.returnGrid())
	random.shuffle(dotLs) # important for not creating a bias twords one side
	for d in dotLs:
		d.step(dot.genStep())