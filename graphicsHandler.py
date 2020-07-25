import graphics as g
import time
from configFile import config

size = 0
win = g.GraphWin()
k = 0

def initGraphics(grid):
    global win, size, k
    size = 500 - (500 % len(grid))
    win = g.GraphWin("Grid", size, size)
    win.setBackground('black')
    k = size/len(grid)

def genGraphics(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j] == 1):
                c = g.Circle(g.Point(k*i+k/2,k*j+k/2),k/2)
                c.setFill('red')
                c.draw(win)
            else:
                c = g.Circle(g.Point(k*i+k/2,k*j+k/2),k/2)
                c.setFill('blue')
                c.draw(win)

    win.getMouse() # Pause to view result
    #time.sleep(0.5)

def drawStep(x, y, dx, dy):
    c = g.Circle(g.Point(k * x + k / 2, k * y + k / 2), k / 2)
    c.setFill('green') if config["colorSteppedPlaces"] else c.setFill('blue')
    c.draw(win)
    c = g.Circle(g.Point(k * dx + k / 2, k * dy + k / 2), k / 2)
    c.setFill('red')
    c.draw(win)