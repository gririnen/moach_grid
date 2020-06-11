import dot
import grid
#import graphicsHandler


gridSide = int(input())
grid = grid.genGrid(gridSide)

d1 = dot.part(1,1)
d1.step(1, 0)

print(grid)