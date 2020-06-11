import dot
#import graphicsHandler

# generates a grid with the input side length 
gridSide = int(input("grid side:"))
dot.genGrid(gridSide)

d1 = dot.part(1,1)
d2 = dot.part(2,0)
dot.printGrid()