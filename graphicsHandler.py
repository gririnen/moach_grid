import graphics as g
import time
def genGraphics(grid):
    size = 500-(500%len(grid))
    win = g.GraphWin("Grid", size, size)
    win.setBackground('black')
    k = size/len(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j] == True):
                c = g.Circle(g.Point(k*i+k/2,k*j+k/2),k/2)
                c.setFill('red')
                c.draw(win)
            else:
                c = g.Circle(g.Point(k*i+k/2,k*j+k/2),k/2)
                c.setFill('blue')
                c.draw(win)

    #win.getMouse() # Pause to view result
    time.sleep(0.5)
    win.close()
