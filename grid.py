def gen_grid(n):
  grid = []
  for i in range(n):
    temp = []
    for j in range(n):
      temp.append(false)
    grid.append(temp)
  return grid
