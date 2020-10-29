from random import randint
import math
from array import *
from copy import copy, deepcopy

grid = []
start = [None] * 2
goal = [None] * 2
hard_traverse_coordinates = [None] * 8

paths = []

ROWS = 120
COLS = 160
# ROWS = 4
# COLS = 7



TOTAL_BLOCKED = 3840


class Cell:
    def __init__(self, col, row, terrain, g_cost, h_cost, f_cost, parent):
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
            # grid[column].append(Cell(row, column, '1', -1, -1, -1, None))

    # for row in range (ROWS):
    #     grid.append([])
    #     for column in range(COLS):
    #         grid[row].append(Cell(row, column, '0', -1, -1, -1))

def make_hard():
    x_hard = 0
    y_hard = 0
    for i in range(8):
        x_hard = randint(0, (COLS-1))
        y_hard = randint(0, (ROWS-1))
        hard_traverse_coordinates[i] = (x_hard, y_hard)
        hard_randomize(x_hard, y_hard)


def hard_randomize(x_hard, y_hard):
    #TODO: make sure you cover directly horizontal/vertical
    #Four Quadrants:
    #Top Left
    for x in range(x_hard, (x_hard-15), -1):
        if(x > -1):
            for y in range(y_hard, (y_hard+15), 1):
                #generate random 
                if(y < ROWS):
                    is_hard = randint(0, 1)
                    if(is_hard == 0):
                        grid[x][y].terrain = '2'

    #Top Right
    for x in range(x_hard, (x_hard+15), 1):
        if (x < COLS):
            for y in range(y_hard, (y_hard+15), 1):
                #generate random 
                if(y < ROWS):
                    is_hard = randint(0, 1)
                    if(is_hard == 0):
                        grid[x][y].terrain = '2'

    #Bottom Left
    for x in range(x_hard, (x_hard-15), -1):
        if(x > -1):
            for y in range(y_hard, (y_hard-15), -1):
                #generate random 
                if(y > -1):
                    is_hard = randint(0, 1)
                    if(is_hard == 0):
                        grid[x][y].terrain = '2'

    
    #Bottom Right
    for x in range(x_hard, (x_hard-15), -1):
        if(x > -1):
            for y in range(y_hard, (y_hard+15), 1):
                #generate random 
                if(y < ROWS):
                    is_hard = randint(0, 1)
                    if(is_hard == 0):
                        grid[x][y].terrain = '2'


        
# def init_path(temp_grid):
#     x = 0
#     y = 0
#     direction = ''
#     side = randint(1, 4)
    
#     if side == 1:
#         x = 0
#         y = randint(0, ROWS-1)
#         direction = 'r'
#     elif side == 2:
#         x = COLS-1
#         y = randint(0, ROWS-1)
#         direction = 'l'
#     elif side == 3:
#         x = randint(0, COLS-1)
#         y = 0
#         direction = 'd'
#     else:
#         x = randint(0, COLS-1)
#         y = ROWS-1
#         direction = 'u'

#     if temp_grid[x][y].terrain == 'a' or temp_grid[x][y].terrain == 'b':
#         # print("terrain: ", temp_grid[x][y].terrain)
#         # for i in range(10):
#         #     print("************************************************")
#         return init_path(temp_grid)
    
#     #printf("starting info: x: ", x, " y: ", y, " dir: ", direction)

#     return (x, y, direction)

# def direct(current_direction):

#     vector = ''
#     prob = randint(0, 100)
#     new_direction = ''

#     if(prob >= 0 and prob < 60):
#         vector = 's'
#     elif(prob >= 60 and prob < 80):
#         vector = 'l'
#     else:
#         vector = 'r'

#     if current_direction == 'l':
#         if vector == 's':
#             new_direction = 'l'
#         elif vector == 'l':
#             new_direction = 'd'
#         else:
#             new_direction = 'u'

#     elif current_direction == 'r':
#         if vector == 's':
#             new_direction = 'r'
#         elif vector == 'l':
#             new_direction = 'u'
#         else:
#             new_direction = 'd'

#     elif current_direction == 'u':
#         if vector == 's':
#             new_direction = 'u'
#         elif vector == 'l':
#             new_direction = 'l'
#         else:
#             new_direction = 'r'

#     else:
#         if vector == 's':
#             new_direction = 'd'
#         elif vector == 'l':
#             new_direction = 'l'
#         else:
#             new_direction = 'r'

#     return new_direction

# def position(x, y, direction, inc):

#     if direction == 'd':
#         y += inc
#     elif direction == 'u':
#         y -= inc
#     elif direction == 'l':
#         x -= inc
#     else:
#         x += inc

#     return (x, y)

# def moving(direction):
#     if direction == 'l':
#         x = -1
#         y = 0
#     elif direction == 'r':
#         x = 1
#         y = 0
#     elif direction == 'u':
#         x = 0
#         y = -1
#     else:
#         x = 0
#         y = 1
#     return (x, y)


# def reached_border(x, y):
#     if x == 0 or x == COLS-1 or y == 0 or y == ROWS-1:
#         return True
#     return False

# def mark_seg(x, y, direction, temp_grid2):
#     inc = moving(direction)
#     x_inc = inc[0]
#     y_inc = inc[1]


#     for i in range(20):
        
#         if (reached_border(x, y)):
#             return i

#         if temp_grid2[x][y].terrain == 'a' or temp_grid2[x][y].terrain == 'b':
#             return -1

        
#         if temp_grid2[x][y].terrain == '1':
#             temp_grid2[x][y].terrain = 'a'
#         elif temp_grid2[x][y].terrain == '2':
#             temp_grid2[x][y].terrain = 'b'

#         # print("2: coordinates: ", x, y, " direction: ", direction, " terrain: ", temp_grid2[x][y].terrain)


#         x += x_inc
#         y += y_inc

#     # 
    
#     return 20



# def make_path(temp_grid, start_point):
#     temp_grid2 = deepcopy(temp_grid)
#     cell_count = 0

#     x = start_point[0]
#     y = start_point[1]
#     direction = start_point[2]

#     #print("make_path called mark seg: ")
#     check = mark_seg(x, y, direction, temp_grid2)

    
#     if check == -1:
#         return -1
#     cell_count += check    

#     x = position(x, y, direction, check)[0]
#     y = position(x, y, direction, check)[1]
    


#     while cell_count < 100 or (not reached_border(x, y)):
#         direction = direct(direction)
#         check = mark_seg(x, y, direction, temp_grid2)
#         if check == -1 or check == 0:
#             return -1

#         cell_count += check    

#         x = position(x, y, direction, check)[0]
#         y = position(x, y, direction, check)[1]
    
#     return temp_grid2

# def create_highway():
#     temp_grid = deepcopy(grid)
    
#     for i in range(4):
#         path_tries = 0
#         check = -1
        
#         while check == -1:
#             if path_tries == 10:
#                 return create_highway()

#             start_point = init_path(temp_grid)
#             check = make_path(temp_grid, start_point)
#             path_tries += 1

#         temp_grid = check

#     return temp_grid

# def make_highway():
#     global grid 
#     grid = create_highway()
#     return 0



def make_blocked():
    x_blocked = 0
    y_blocked = 0
    num_blocked = 0
    while(num_blocked < TOTAL_BLOCKED):
        x_blocked = randint(0, COLS-1)
        y_blocked = randint(0, ROWS-1)

        if((grid[x_blocked][y_blocked].terrain != 'a') and (grid[x_blocked][y_blocked].terrain != 'b') and (grid[x_blocked][y_blocked].terrain != '0')):
            grid[x_blocked][y_blocked].terrain = '0'
            num_blocked = num_blocked + 1
        

def make_start():
    
    while True:
        is_top = randint(0,1)
        is_left = randint(0,1)
        start_x = 0
        start_y = 0
        if(is_top):
            start_y = randint(0, 20)
        else:
            start_y = randint(100, ROWS-1)
        if(is_left):
            start_x = randint(0, 20)
        else:
            start_x = randint(140, COLS-1)

        #TODO: out of bounds error here sometimes. I'm not sure why
        if(grid[start_x][start_y].terrain != '0'):
            start[0] = start_x
            start[1] = start_y
            return

def make_goal():
    start_x = start[0]
    start_y = start[1]
    goal_x = 0
    goal_y = 0
    
    

    #Set goal, if fail repeat
    while True:
        is_top = randint(0,1)
        is_left = randint(0,1)

        if(is_top):
            goal_y = randint(0, 20)
        else:
            goal_y = randint(100, ROWS-1)
        if(is_left):
            goal_x = randint(0, 20)
        else:
            goal_x = randint(140, COLS-1)

        #TODO: SOmetimes out of bounds. I don't know why
        if(grid[goal_x][goal_y].terrain != '0'):
            distance =  math.sqrt((goal_x - start_x)**2 + (goal_y - start_y)**2)
            if(distance >= 100):
                
                #Set the goal at (goal_x, goal_y)
                goal[0] = goal_x
                goal[1] = goal_y
                return

def get_neighbors(x, y):
    neighbors = []
    
    #Diagonal Neighbors
    if(x-1 > -1) and (y-1 > -1):
        if(grid[x-1][y-1].terrain != '0'):
            neighbors.append(grid[x-1][y-1])
    if(x-1 > -1) and (y+1 < ROWS):
        if(grid[x-1][y+1].terrain != '0'):
            neighbors.append(grid[x-1][y+1])
    if(x+1 < COLS) and (y-1 > -1):
        if(grid[x+1][y-1].terrain != '0'):
            neighbors.append(grid[x+1][y-1])
    if(x+1 < COLS) and (y+1 < ROWS):
        if(grid[x+1][y+1].terrain != '0'):
            neighbors.append(grid[x+1][y+1])
    
    #Horizontal/Vertical Neighbors
    if(x-1 > -1):
        if(grid[x-1][y].terrain != '0'):
            neighbors.append(grid[x-1][y])
    if(x+1 < COLS):
        if(grid[x+1][y].terrain != '0'):
            neighbors.append(grid[x+1][y])
    if(y-1 > -1):
        if(grid[x][y-1].terrain != '0'):
            neighbors.append(grid[x][y-1])
    if(y+1 < ROWS):
        if(grid[x][y+1].terrain != '0'):
            neighbors.append(grid[x][y+1])
    
    return neighbors

#print grid
def print_grid():
    for row in range (ROWS):
        for column in range (COLS):
            print (grid[column][row].terrain, end = ' ')
        print("\n")
        
#Output File for Grid
def write_grid_file(name):
    my_file = open(name, "w")
    
    start_str_list = ['(', str(start[0]), ', ', str(start[1]), ')']
    start_coordinates = "".join(start_str_list)
    print(start_coordinates)
    my_file.write(start_coordinates)

    goal_str_list = ['(', str(goal[0]), ', ', str(goal[1]), ')']
    goal_coordinates = "".join(goal_str_list)
    my_file.write(goal_coordinates)
    
    for i in range(8):
        string_hard = ''.join(str(hard_traverse_coordinates[i]))
        my_file.write(string_hard)
    for rows in range(ROWS):
        line = grid[rows]
        for cols in range(COLS):
               my_file.write(grid[cols][rows].terrain)
        my_file.write("\n") 
    my_file.close()
    return my_file

#Read File for Grid
#Ex:
#(1, 2) -start
#(3, 2) -goal
#(1, 2) -1st hard to traverse
#(7, 2) -2nd hard to traverse
# ...
#(4, 3) -8th hard to traverse
#111...0 -160 characters
def read_grid_file(file):
    with open(file, 'r') as f:
        start_coordinates = f.readline()

        end = start_coordinates.find(',')
        start[0] = int(start_coordinates[1:end])

        end2 = start_coordinates.find(')')
        start[1] = int(start_coordinates[end+2:end2])
        print(start)


        goal_coordinates = f.readline()

        end = goal_coordinates.find(',')
        goal[0] = int(goal_coordinates[1:end])

        end2 = goal_coordinates.find(')')
        goal[1] = int(goal_coordinates[end+2:end2])
        print(goal)

        for i in range(8):
            #Take coordinates for centers and put them in a tuple
            hard_traverse_coordinates.append(f.readline())
            
            #hard_traverse_coordinates.append(f.readline())
        #make_grid(ROWS, COLS)
        for rows in range(ROWS):
            line = f.readline()
            for cols in range(COLS):
                grid[cols][rows].terrain = line[cols] 


#I didn't allow Corner Squares
def choose_highway_start():
    side = randint(0, 3)
    x_coordinate = -1
    y_coordinate = -1
    direction = '-'

    if(side == 0): #moving left
        x_coordinate = COLS-1
        y_coordinate = randint(1, (ROWS-2))
        direction = 0 #left
    elif(side == 1): #moving up
        x_coordinate = randint(1, (COLS - 2))
        y_coordinate = ROWS-1
        direction = 1 #up
    elif(side == 2): #moving right
        x_coordinate = 0
        y_coordinate = randint(1, (ROWS-2))
        direction = 2 #right
    else: #moving down
        x_coordinate = randint(1, (COLS - 2))
        y_coordinate = 0
        direction = 3 #down
    
    start = (x_coordinate, y_coordinate, direction)
    return start


def design_all_highways():
    fail_counter = 0
    num_highways = 0
    while(num_highways<4):
        highway_coordinates = design_highway()
        # print(highway_coordinates)
        if(highway_coordinates == False):
            fail_counter = fail_counter + 1
            if(fail_counter >= 10):
                reset_all_highways()
                num_highways = 0
        else:
            num_highways = num_highways + 1

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
        if(grid[x][y].terrain == 'a' or grid[x][y].terrain == 'b'):
            reset_highway(highway_coordinates)
            return False
        elif(grid[x][y].terrain == '1'):
            grid[x][y].terrain = 'a'
        elif(grid[x][y].terrain == '2'):
            grid[x][y].terrain = 'b'
        highway_coordinates.append((x, y))
        highway_length = highway_length + 1
        if(highway_length >= 20):
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

        #Get off elbow square
        if(direction == 0):
            x = x-1
        elif(direction == 1):
            y = y-1
        elif(direction == 2):
            x = x+1
        elif(direction == 3):
            y = y+1
            
        count = 0
        while(True):
            if(grid[x][y].terrain == 'a' or grid[x][y].terrain == 'b'):
                reset_highway(highway_coordinates)
                return False
            elif(grid[x][y].terrain == '1'):
                grid[x][y].terrain = 'a'
            elif(grid[x][y].terrain == '2'):
                grid[x][y].terrain = 'b'
            highway_coordinates.append((x, y))
            highway_length = highway_length + 1
            if((x == 0) or (x == (COLS - 1)) or (y == 0) or (y == (ROWS - 1))):
                if(highway_length >= 100):
                    return highway_coordinates
                else:
                    reset_highway(highway_coordinates)
                    return False
            if(count >= 20):
                break

            if(direction == 0):
                x = x-1
            elif(direction == 1):
                y = y-1
            elif(direction == 2):
                x = x+1
            elif(direction == 3):
                y = y+1
            count = count+1
            

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
    for row in range (ROWS):
        for column in range (COLS):
            if(grid[column][row].terrain == 'a'):
                grid[column][row].terrain = '1'
            elif(grid[column][row].terrain == 'b'):
                grid[column][row].terrain = '2'
