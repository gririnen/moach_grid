import dot
import random
#import graphicsHandler

# generates a grid with the input side length 
gridSide = int(input("grid side:"))
dot.genGrid(gridSide)

dotLs = []
dotLs.append(dot.part([1,1]))
dotLs.append(dot.part([1,2]))
dotLs.append(dot.part([2,1]))
dotLs.append(dot.part([2,2]))

print(dot.returnGrid())
random.shuffle(dotLs) # important for not creating a bias twords one side
for d in dotLs:
	d.step(dot.genStep())
print(dot.returnGrid())