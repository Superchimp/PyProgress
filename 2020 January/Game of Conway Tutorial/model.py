import random, view

height = 100
width = 100

grid_model = [0] * height
next_grid_model = [0] * height

for i in range(height):
    grid_model[i] = [0] * width
    next_grid_model[i] = [0] * width
    
def randomize(grid, width, height):
    for i in range(0,height):
        for j in range(0, width):
            grid_model[i][j] = random.randint(0,1)

#randomize(grid_model, width, height)
    
def next_gen():
    global grid_model, next_grid_model
    
    for i in range(0, height):
        for j in range(0,width):
            cell = 0
            #print("Checking cell", i, j)
            count = count_neighbours(grid_model, i, j)
            
            if grid_model[i][j] == 0:
                if count == 3:
                    cell = 1
            elif grid_model[i][j] == 1:
                if count == 2 or count == 3:
                    cell = 1
            next_grid_model[i][j] = cell
            #print("New Value is", next_grid_model[i][j])
    temp = grid_model
    grid_model = next_grid_model
    next_grid_model = temp
                    
def count_neighbours(grid, row, col):
    count = 0
    
    if row -1 >= 0:
        count = count + grid[row -1][col]
    if row -1 >= 0 and col -1 >=0:
        count = count + grid[row -1][col -1]
    if row -1 >= 0 and col +1 < width:
        count = count + grid[row -1][col +1]
    if col -1 >= 0:
        count = count + grid[row][col -1]
    if col +1 < width:
        count = count + grid[row][col +1]
    if row +1 < height:
        count = count + grid[row +1][col]
    if row +1 < height and col -1 >= 0:
        count = count + grid[row +1][col -1]
    if row +1 < height and col +1 < width:
        count = count +grid[row +1][col +1]
    return count

def kill_grid():
    for i in range(0,height):
        for j in range(0,width):
            grid_model[i][j] = 0

def load_pattern(pattern, x_offset=0, y_offset=0):
    global grid_model
    
    j = y_offset
    kill_grid
    for row in pattern:
        i = x_offset
        for value in row:
            grid_model[i][j] = value
            i = i + 1
        j = j + 1

glider_pattern = [[0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0]]

glider_gun_pattern = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



if __name__ == "__main__":
    next_gen()