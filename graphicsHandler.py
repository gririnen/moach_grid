import graphics as g
import time
from configFile import config

size = 0
win = g.GraphWin() #generates deafult graphic window, required to start the program
k = 0
#all parameters will be set different values on initGraphics

def initGraphics(grid):
    """initGraphics(int[][]) -> void
    generates the graphic window"""
    global win, size, k
    size = 500 - (500 % len(grid)) #limits pixel size to 500 pixels, makes sure the particles dont take fractions of pixels
    win = g.GraphWin("Grid", size, size) #generates the window
    win.setBackground('black') #more visible with black background
    k = size/len(grid) #the diameter of each particle in pixels

def genGraphics(grid):
    """genGraphics(int[][]) -> void
    updates window with new grid.data, only use at start or when changing the grid completely
    as this process is quite slow due to processing speed"""
    for i in range(len(grid)):
        for j in range(len(grid)):
            #goes through every index in grid.data
            if(grid[i][j] == 1):
                c = g.Circle(g.Point(k*i+k/2,k*j+k/2),k/2) #generates circle with k diameter in pixels at i,j
                c.setFill('red') #if there is a particle the circle is red
                c.draw(win)
            else:
                c = g.Circle(g.Point(k*i+k/2,k*j+k/2),k/2) #generates circle with k diameter in pixels at i,j
                c.setFill('blue') #if no particle the circle is blue
                c.draw(win)

    win.getMouse() # Pause to view result
    #time.sleep(0.5)

def drawStep(x, y, dx, dy):
    """drawstep(int,int,int,int) -> void
    takes old particle location and the new coords, and changes the color of the circles"""
    c = g.Circle(g.Point(k * x + k / 2, k * y + k / 2), k / 2) #old particle location
    c.setFill('green') if config["colorSteppedPlaces"] else c.setFill('blue') #if colorSteppedPlaces in config then it paint the circle green, else it's blue
    c.draw(win)
    c = g.Circle(g.Point(k * dx + k / 2, k * dy + k / 2), k / 2) #new particle location
    c.setFill('red') #colors new particle location in red
    c.draw(win)
