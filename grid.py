def genGrid(gridSide):
  grid = []
  for i in range(gridSide):
    temp = []
    for j in range(gridSide):
      temp.append(false)
    grid.append(temp)
  return grid
