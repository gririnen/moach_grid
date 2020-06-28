import dot
import random
import graphicsHandler as gH

# generates a grid with the input side length 
gridSide = int(input("grid side:"))
dot.genGrid(gridSide)
gH.genGraphics(dot.returnGrid())

dotLs = []
dotLs.append(dot.part([4,4]))
dotLs.append(dot.part([4,5]))
dotLs.append(dot.part([5,4]))
dotLs.append(dot.part([5,5]))

gH.genGraphics(dot.returnGrid())
while True:
	random.shuffle(dotLs) # important for not creating a bias twords one side
	for d in dotLs:
		d.step(dot.genStep())
	gH.genGraphics(dot.returnGrid())