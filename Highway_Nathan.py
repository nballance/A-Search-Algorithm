# from Map import make_grid
from random import randint
COLS = 160
ROWS = 120

grid = []

class Cell:
    def __init__(self, row, col, terrain, g_cost, h_cost, f_cost, parent):
        self.row = row
        self.col = col
        self.terrain = terrain
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = f_cost
        self.parent = parent

def make_grid():
    for column in range (COLS):
        grid.append([])
        for row in range(ROWS):
            grid[column].append(Cell(column, row, '1', -1, -1, -1, None))

def choose_highway_start():
    side = randint(0, 3)
    x_coordinate = -1
    y_coordinate = -1
    direction = '-'

    if(side == 0): #moving left
        x_coordinate = COLS-1
        y_coordinate = randint(0, (ROWS-1))
        direction = 0 #left
    elif(side == 1): #moving up
        x_coordinate = randint(0, (COLS - 1))
        y_coordinate = ROWS-1
        direction = 1 #up
    elif(side == 2): #moving right
        x_coordinate = 0
        y_coordinate = randint(0, (ROWS-1))
        direction = 2 #right
    else: #moving down
        x_coordinate = randint(0, (COLS - 1))
        y_coordinate = 0
        direction = 3 #down
    
    start = (x_coordinate, y_coordinate, direction)
    return start


def design_all_highways():
    fail_counter = 0
    for i in range(1, 4):
        if(design_highway() == False):
            fail_counter = fail_counter + 1
            if(fail_counter >= 10):
                reset_all_highways()

def design_highway():
    start_data = choose_highway_start()
    start_coordinate = (start_data[0], start_data[1])
    direction = start_data[2]

    highway_length = 0
    highway_coordinates = []

    x = start_coordinate[0]
    y = start_coordinate[1]
    while(True):
        #check and set terrain
        if(grid[x][y].terrain == '0' or grid[x][y].terrain == 'a' or grid[x][y].terrain == 'b'):
            reset_highway(highway_coordinates)
            return False
        elif(grid[x][y].terrain == '1'):
            grid[x][y].terrain == 'a'
        elif(grid[x][y].terrain == '2'):
            grid[x][y].terrain == 'b'
        highway_coordinates.append((x, y))
        highway_length = highway_length + 1
        if(highway_length == 20):
            break

        if(direction == 0):
            x = x-1
        elif(direction == 1):
            y = y-1
        elif(direction == 2):
            x = x+1
        elif(direction == 3):
            y = y+1
        


    while(True):
        #We double count the elbows in the highway
        highway_length = highway_length + 1

        #Choose direction
        probability = randint(1, 100)
        if(probability <= 60):
            pass
        elif(probability > 60 and probability <= 80): #turn right
            if(direction == 3):
                direction = 0
            else:
                direction = direction + 1
        else: #turn left
            if(direction == 0):
                direction = 3
            else:
                direction = direction - 1

        for i in range(20):
            if(grid[x][y].terrain == 0 or grid[x][y].terrain == 'a' or grid[x][y].terrain == 'b'):
                reset_highway(highway_coordinates)
                return False
            elif(grid[x][y].terrain == '1'):
                grid[x][y].terrain == 'a'
            elif(grid[x][y].terrain == '2'):
                grid[x][y].terrain == 'b'
            highway_coordinates.append((x, y))
            highway_length = highway_length + 1
            if((x == 0) or (x == (COLS - 1)) or (y == 0) or (y == (ROWS - 1))):
                if(highway_length >= 100):
                    return highway_coordinates
                else:
                    reset_highway(highway_coordinates)
                    return False
            if(direction == 0):
                x = x-1
            elif(direction == 1):
                y = y-1
            elif(direction == 2):
                x = x+1
            elif(direction == 3):
                y = y+1
            

def reset_highway(highway_coordinates):
    num_coordinates = len(highway_coordinates)
    x_coordinate = -1
    y_coordinate = -1
    for i in range (num_coordinates):
        x_coordinate = highway_coordinates[i][0]
        y_coordinate = highway_coordinates[i][1]
        if(grid[x_coordinate][y_coordinate].terrain == 'a'):
            grid[x_coordinate][y_coordinate].terrain = '1'
        elif(grid[x_coordinate][y_coordinate].terrain == 'b'):
            grid[x_coordinate][y_coordinate].terrain = '2'

#Lazy approach is iterate through grid and reset all a's to 1 and b's to 2
#Other approach is using the highway tuple, but I don't feel like getting that to work rn
def reset_all_highways():
    pass

def make_all_highways():
    pass


# print(choose_highway_start())

make_grid()
print(grid[100][100])
print(design_highway())


# def tuple_experiment():
#     #highway_coordinates = (((1, 2),(2, 2)), ((6, 5), (6, 6)))
#     highway_coordinates = []
#     highway_coordinates.append((1, 2))
#     highway_coordinates.append((3, 3))
#     #highway_coordinates = ((1, 2),(2, 2), (6, 5), (6, 6))
    
#     return highway_coordinates

# data = tuple_experiment()
# print(data)
# print(data[0][1], data[1])
