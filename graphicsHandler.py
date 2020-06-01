from graphics import *
import playGround as pg
import grid

win = GraphWin("Window", 100, 100)
grid = grid.genGrid(10)

def genGraphics():
  #print(grid)
  for i in range(10):
    for j in range(10):
      print(grid[i][j])
      if(grid[i][j] = True):
        print("Here")
        x = grid[i][j].x
        y = grid[i][j].y
        point = Point(x,y)
        cir = Circle(point, 1)
        cir.setfill(color_rgb(255, 0, 0))
        cir.draw(win)
        win.getMouse()
        win.close

#print(grid)
#genGraphics()
print(" ")
gridSide = int(input())
