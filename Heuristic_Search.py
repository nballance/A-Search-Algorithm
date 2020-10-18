from heapq import heapify, heappush, heappop
from Map import *
import math
WEIGHT = 1


# def a_search():
#     current = grid[start[0], start[1]]
#     open_list = []
#     closed_list = []

    # heapify(open_list)

    # while (current != goal): 
    #     neighbors = get_neighbors(current)
    #     samePriority = []
    #     length = len(neighbors)
    #     for i in range(length):
    #         cur_neighbor = neighbors[i]
    #         if ((neighbors[i] not in closed_list) and (neighbors[i] not in open_list)):
    #             calculate_h_val(neighbors[i])
    #             calculate_g_val(neighbors[i], neighbors[i].parent)
    #             heappush(open_list, (neighbors[i].f_cost, neighbors[i]))
                
    #     heapify(open_list)
                
#c              

def a_search():
    open_list = []
    closed_list = []

    #Calculate heuristic distance of start vertex to destination (h)
    grid[start[0], start[1]].g_cost = 0
    grid[start[0], start[1]].h_cost = calculate_h_val(grid[start[0], start[1]])

    #Calculate f value for start vertex (f = g + h, where g = 0)
    grid[start[0], start[1]].f_cost = calculate_f_val(grid[start[0], start[1]])

    # |WHILE current vertex is not destination
    current = grid[start[0], start[1]]
    destination = grid[goal[0], goal[1]]

    while(current != destination):
        neighbors = get_neighbors()
    # |  FOR Each vertex adjacent to current
        num_neighbors = neighbors.length()
        for i in range(0, num_neighbors-1):
        # |  |    IF vertex not in closed list and not in open List THEN
            if ((neighbors[i] not in closed_list) and (neighbors[i] not in open_list)):
                
                neighbors[i].parent = current

            # |  |    |    Calculate distance from start (g)
                calculate_g_val(neighbors[i])
            # |  |    |    Calculate distance to goal (h)
                calculate_h_val(neighbors[i])    
            # |  |    |    Calculate f value (f = g + h)  
                calculate_f_val(neighbors[i])  
            # |  |    |    Add vertex to open list
                open_list.append(neighbors[i])
            elif(neighbors[i] in open_list):
                #see if the new g value is less than the previous g value
                old_parent = neighbors[i].parent
                neighbors[i].parent = current

                if(neighbors[i].g_cost <= calculate_g_val(neighbors[i])):
                    neighbors[i].parent = old_parent
        heapify(open_list)

    # |  |    |   IF new f value < existing f value or there is no existing f value Then
    # |  |    |    |    Update f value
    # |  |    |    |    Set parent to be current vertex
    # |  |    |    END IF 
    # |  |    END IF


    # |  NEXT adjacent vertex
        closed_list.append(current)
    # |  Add current vertex to closed list
        current = open_list.pop()
        while(open_list.peak()):
            next_cell = open_list.peak()
            if(next_cell.h_cost < current.h_cost):
                open_list.append(current)
                current = open_list.pop()
        heapify(open_list)

    # |  Remove vertex to closed list
    # |  Remove vertex with lowest f value from open list and make it current
    # |End WHILE   


#Returns the cost from starting node
def calculate_g_val(cell):
    terrain1 = cell.terrain
    terrain2 = cell.parent.terrain
    highway = False
    diagonal = False
    cost = 0

    #Diagonal or not
    if((cell.row != cell.parent.row) and (cell.col != cell.parent.col)):
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
            cost = (math.sqrt(2) + math.sqrt(8)) /2
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

    return cell.parent.g_cost + cost 
    

#Cost to ending node
def calculate_h_val(cell):
    distance_to_goal = distance(cell)
    cell.h_cost = (distance_to_goal[0] * math.sqrt(2) + distance_to_goal[1]) 
    grid[cell[cell.row], cell[cell.col]].h_cost = cell.h_cost

#G Cost + H Cost
#Check parent
def calculate_f_val(cell):
    cell.f_cost = cell.g_cost + cell.h_cost
    grid[cell[cell.row], cell[cell.col]].f_cost = cell.f_cost

#Number of diagonals and number of straight path

#Number of diagonals and number of straight path

#Number of diagonals and number of straight path
def distance(cell):
    num_diagonals = 0
    num_straights = 0

    cell_coordinate = []
    total_distance = []

    cell_coordinate[0] = cell.col #x val
    cell_coordinate[1] = cell.row #y val
    
    #Finds the shortest path from the cell parameter to the goal
    while(not(cell_coordinate[0] == goal[0] and cell_coordinate[1] == goal[1]) ):
    
        #Diagonal up-right
        if(cell_coordinate[0] < goal[0] and cell_coordinate[1] < goal[1] ):
            num_diagonals += 1
            cell_coordinate[0] += 1
            cell_coordinate[1] += 1
        #Diagonal up-left
        elif(cell_coordinate[0] > goal[0] and cell_coordinate[1] < goal[1] ):
            num_diagonals += 1
            cell_coordinate[0] -= 1
            cell_coordinate[1] += 1
        #Diagonal down-left
        elif(cell_coordinate[0] > goal[0] and cell_coordinate[1] > goal[1] ):
            num_diagonals += 1
            cell_coordinate[0] -= 1
            cell_coordinate[1] -= 1
        #Diagonal down-right
        elif(cell_coordinate[0] < goal[0] and cell_coordinate[1] > goal[1] ):
            num_diagonals += 1
            cell_coordinate[0] += 1
            cell_coordinate[1] -= 1

        #Left
        elif(cell_coordinate[0] > start[0] and cell_coordinate[1] == goal[1]):
            num_straights += 1
            cell_coordinate[0] -= 1
        #Right
        elif(cell_coordinate[0] < start[0] and cell_coordinate[1] == goal[1]):
            num_straights += 1
            cell_coordinate[0] -= 1
        #Down 
        elif(cell_coordinate[0] == start[0] and cell_coordinate[1] < goal[1]):
            num_straights += 1
            cell_coordinate[1] += 1
        #Up
        elif(cell_coordinate[0] == start[0] and cell_coordinate[1] > goal[1]):
            num_straights += 1
            cell_coordinate[1] -= 1
        
    total_distance[0] = num_diagonals
    total_distance[1] = num_straights
    #return ("Number of diagonals: ", num_diagonals, "Number of straights: ", num_straights)
    return total_distance
