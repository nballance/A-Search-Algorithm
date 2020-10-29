from heapq import *
from operator import index
from Map import *
import math
from queue import PriorityQueue

import operator



A_WEIGHT = 1     
# start = (0, 0)
# goal = (6, 3)


#Uniform Cost Search

# def u_search():
#     count = 0
#     cost = 0
#     visited = []
#     fringe = PriorityQueue()
#     current = grid[start[0], start[1]]
#     destination = grid[goal[0], goal[1]]

#     while (count < 120*160):
#         neighbors = get_neighbors(current)
        
#         for i in range(0, neighbors.length-1):
#             #set the parent for the neighbors
#             neighbors[i].parent = current
#             if(neighbors[i] in fringe):
#                 fringe = searchFringe
                
            
#             fringe.put(calculate_g_val(neighbors[i]), neighbors[i])

#     pass

def uniform_search():
    a_search(0)

# def searchFringe(fringe, cell):
#     new_fringe = PriorityQueue()
#     while not fringe.empty():
#         next_item = fringe.get()
#         if(next_item.g_cost > calculate_g_val()):
#             next_item.g_cost =  cell.g_cost
#             new_fringe.put(cell.g_cost)


#A*_Algorithm (weight of 1)
def a_search_standard():
    a_search(A_WEIGHT)


def a_search(weight):

    open_list = []
    
    closed_list = []
    
    x_start = start[0]
    y_start = start[1]
    x_goal = goal[0]
    y_goal = goal[1]

    # print("x_start: ", x_start)
    # print("y_start: ", y_start)
    # print("x_goal: ", x_goal)
    # print("y_goal: ", y_goal)

    

    #Calculate heuristic distance of start vertex to destination (h)
    grid[x_start][y_start].g_cost = 0
    grid[x_start][y_start].h_cost =calculate_h_val(x_start, y_start, weight)

    #Calculate f value for start vertex (f = g + h, where g = 0)
    grid[x_start][y_start].f_cost = calculate_f_val(x_start, y_start)

    # |WHILE current vertex is not destination
    current = grid[x_start][y_start]
    destination = grid[x_goal][y_goal]

    while(current is not (destination)):
    # while(current.row != x_goal and current.col != y_goal):
        neighbors = get_neighbors(current.col, current.row)
        
        # print("Current Cell: ", current.row, current.col, x_start, y_start)
        # for i in range (len(neighbors)):
        #     print(neighbors[i].terrain)
        # print("Current Neighbors: ", neighbors)

    # |  FOR Each vertex adjacent to current
        num_neighbors = len(neighbors)
        # print("The Number of Neighbors: ", num_neighbors)
        
        for i in range (num_neighbors):
            index_in_open = -1
        # |  |    IF vertex not in closed list and not in open List THEN
            in_closed = False
            in_open = False
            for j in range(len(closed_list)):

                if((neighbors[i].row == closed_list[j].row) and (neighbors[i].col == closed_list[j].col)):
                    in_closed = True
                    break
            for j in range(len(open_list)):
                # if(neighbors[i].row == open_list[j].get('cell').row and (neighbors[i].col == open_list[j].get('cell').col)):
                if(neighbors[i].row == open_list[j][0].row and neighbors[i].col == open_list[j][0].col):
                    index_in_open = j
                    in_open = True
                    break
            # if ((neighbors[i] not in closed_list) and (neighbors[i] not in open_list)):
            if(not in_open and not in_closed):    
                row_num = neighbors[i].row
                col_num = neighbors[i].col
                grid[col_num][row_num].parent = current

                # neighbors[i].parent = current

            # |  |    |    Calculate distance from start (g)
                neighbors[i].g_cost = calculate_g_val(neighbors[i].col, neighbors[i].row)

            # |  |    |    Calculate distance to goal (h)
                neighbors[i].h_cost = calculate_h_val(neighbors[i].col, neighbors[i].row, weight)    
            # |  |    |    Calculate f value (f = g + h)  
                neighbors[i].f_cost = calculate_f_val(neighbors[i].col, neighbors[i].row)  
            # |  |    |    Add vertex to open list
                # open_list.append( {'cell': neighbors[i], 'f': neighbors[i].f_cost, 'h': neighbors[i].h_cost})
                open_list.append((neighbors[i], neighbors[i].f_cost, neighbors[i].h_cost))
            
            elif(in_open):
                #see if the new f value is less than the previous f value
                #See if the new h val is less than prev
                old_h_val = neighbors[i].h_cost
                old_f_val = neighbors[i].f_cost
                old_g_val = neighbors[i].g_cost
                old_parent = neighbors[i].parent

                row_num = neighbors[i].row
                col_num = neighbors[i].col
                grid[col_num][row_num].parent = current

                neighbors[i].parent = current
                neighbors[i].h_cost = calculate_h_val(neighbors[i].col, neighbors[i].row, weight)
                neighbors[i].g_cost = calculate_g_val(neighbors[i].col, neighbors[i].row)
                neighbors[i].f_cost = calculate_f_val(neighbors[i].col, neighbors[i].row)
                
                #update f val in open list
                if(neighbors[i].f_cost < old_f_val):
                    neighbors[i].parent = current
                    open_list.remove(open_list[index_in_open])                 
                    open_list.append((neighbors[i], neighbors[i].f_cost, neighbors[i].h_cost))
                elif(neighbors[i].f_cost == old_f_val):
                    if(neighbors[i].h_cost < old_h_val):
                        neighbors[i].parent = current
                        #update the old h value of cell that has the same f value
                        # open_list.append({'cell': neighbors[i], 'f': neighbors[i].f_cost, 'h': neighbors[i].h_cost})
                        open_list.remove(open_list[index_in_open])                 
                        open_list.append((neighbors[i], neighbors[i].f_cost, neighbors[i].h_cost))
                    else:
                        row_num = neighbors[i].row
                        col_num = neighbors[i].col

                        neighbors[i].parent = old_parent
                        grid[col_num][row_num].parent = old_parent
                        neighbors[i].h_cost = old_h_val
                        grid[col_num][row_num].h_cost = old_h_val
                        neighbors[i].g_cost = old_g_val
                        grid[col_num][row_num].g_cost = old_g_val
                        neighbors[i].f_cost = old_f_val
                        grid[col_num][row_num].f_cost = old_f_val
                else:
                    row_num = neighbors[i].row
                    col_num = neighbors[i].col

                    neighbors[i].parent = old_parent
                    grid[col_num][row_num].parent = old_parent
                    neighbors[i].h_cost = old_h_val
                    grid[col_num][row_num].h_cost = old_h_val
                    neighbors[i].g_cost = old_g_val
                    grid[col_num][row_num].g_cost = old_g_val
                    neighbors[i].f_cost = old_f_val
                    grid[col_num][row_num].f_cost = old_f_val



        closed_list.append(current)
  
        # sorted(open_list, key=mySort)
        # open_list.sort(reverse=False, key=mySort)
        open_list.sort(key = operator.itemgetter(1, 2))
        # current  = open_list.pop().get('cell')
        # current_tuple = open_list.remove(open_list[0])
        current = open_list[0][0]
        open_list.remove(open_list[0])        

    # |  Remove vertex to closed list
    # |  Remove vertex with lowest f value from open list and make it current
    # |End WHILE   
    # print("Parent terrain: ", grid[x_goal][y_goal].parent.terrain, "Parent x: ", grid[x_goal][y_goal].parent.row, "Parent y: ", grid[x_goal][y_goal].parent.col)
    # print("Parent terrain: ", grid[x_goal][y_goal].parent.parent.terrain, "Parent x: ", grid[x_goal][y_goal].parent.parent.row, "Parent y: ", grid[x_goal][y_goal].parent.parent.col)

    
    #  grid[x_goal][y_goal]
    path_coordinates(x_goal, y_goal)


def mySort(Cell):
    #Sorts by f, need to sort by h too
    return Cell['f']

def path_coordinates(x_goal, y_goal):
    current = grid[x_goal][y_goal]
    
    while(current is not None):
        paths.append((current.col, current.row))
        # path.append((current.row, current.col))

        print("X of current: ", current.col, "Y of current: ", current.row)
        
        current = current.parent
    # return path

#Returns the cost from starting node
#set parent before calculate_g_val is called
def calculate_g_val(x, y):
    terrain1 = grid[x][y].terrain
    terrain2 = grid[x][y].parent.terrain
    
    # print(grid[x][y], grid[x][y].parent)
    # print("The parent of ", grid[x][y].row, grid[x][y].col, " is ", grid[x][y].parent.row, grid[x][y].parent.col)
    
    highway = False
    diagonal = False
    cost = 0

    #Diagonal or not
    if((x != grid[x][y].parent.col) and (y != grid[x][y].parent.row)):
        diagonal = True

    if((terrain1 == 'a' or terrain1 =='b') and (terrain2 == 'a' or terrain2 =='b')):
        highway = True
    
    #Regular to Regular
    if((terrain1 == '1' or terrain1 =='a') and (terrain2 == '1' or terrain2 =='a') ):
        if(diagonal):
            cost = math.sqrt(2)
        else:
            cost = 1 

    #Regular to Hard/Hard to Regular
    if(((terrain1 == '1' or terrain1 =='a') and (terrain2 == '2' or terrain2 =='b')) or ((terrain1 == '2' or terrain1 =='b') and (terrain2 == '1' or terrain2 =='a'))):
        if(diagonal):
            cost = ((math.sqrt(2) + math.sqrt(8)) /2)
            #Should be 2.1213
        else:
            cost = 1.5 
    #Hard to Hard
    if((terrain1 == '2' or terrain1 =='b') and (terrain2 == '2' or terrain2 =='b') ):
        if(diagonal):
            cost = math.sqrt(8)
        else:
            cost = 2
    if(highway):
        cost = cost/4

    g_val_variable = round((grid[x][y].parent.g_cost + cost), 5)
    grid[x][y].g_cost = g_val_variable
    return grid[x][y].g_cost
    

#Cost to ending node
def calculate_h_val(x, y, weight):
    distance_to_goal = distance(x, y)

    # print(distance_to_goal)
    
    h_val_variable = round(distance_to_goal[0] * weight * math.sqrt(2) + distance_to_goal[1] * weight, 5)
    grid[x][y].h_cost = h_val_variable
    
    return grid[x][y].h_cost

#G Cost + H Cost
#Check parent
def calculate_f_val(x, y):
    f_val_variable = round(grid[x][y].g_cost + grid[x][y].h_cost, 5)
    grid[x][y].f_cost = f_val_variable
    # grid[cell[cell.row], cell[cell.col]].f_cost = cell.f_cost
    return grid[x][y].f_cost

#Number of diagonals and number of straight path
def distance(x, y):
    num_diagonals = 0
    num_straights = 0

    # cell_coordinate = []
    total_distance = [None] * 2

    # cell_coordinate[0] = cell.col #x val
    # cell_coordinate[1] = cell.row #y val
    
    #Finds the shortest path from the cell parameter to the goal
    while(not(x == goal[0] and y == goal[1]) ):
    
        # print(x, y)
        
        #Diagonal up-right
        if(x < goal[0] and y > goal[1] ):
            num_diagonals += 1
            x += 1
            y -= 1
        #Diagonal up-left
        elif(x > goal[0] and y > goal[1] ):
            num_diagonals += 1
            x -= 1
            y -= 1
        #Diagonal down-left
        elif(x > goal[0] and y < goal[1] ):
            num_diagonals += 1
            x -= 1
            y += 1
        #Diagonal down-right
        elif(x < goal[0] and y < goal[1] ):
            num_diagonals += 1
            x += 1
            y += 1

        #Left
        elif(x > goal[0] and y == goal[1]):
            num_straights += 1
            x -= 1
        #Right
        elif(x < goal[0] and y == goal[1]):
            num_straights += 1
            x += 1
        #Down 
        elif(x == goal[0] and y < goal[1]):
            num_straights += 1
            y += 1
        #Up
        elif(x == goal[0] and y > goal[1]):
            num_straights += 1
            y -= 1
        
    total_distance[0] = num_diagonals
    total_distance[1] = num_straights
    #return ("Number of diagonals: ", num_diagonals, "Number of straights: ", num_straights)
    return total_distance
