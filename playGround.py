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

genMidSquare(5)

gH.genGraphics(dot.returnGrid())
counter = 0
while dot.killProgram == False:
	random.shuffle(dotLs) # important for not creating a bias twords one side
	for d in dotLs:
		if(dot.killProgram == True):
			break
		counter += 1
		x,y = d.x,d.y
		d.step(dot.genStep())
		gH.drawStep(x,y,d.x,d.y)
	#gH.genGraphics(dot.returnGrid())
print("steps:", counter)