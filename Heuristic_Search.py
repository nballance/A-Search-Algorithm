from heapq import heapify, heappush, heappop
from Map import *
import math
WEIGHT = 1
#Initialize open and closed lists
#Make the start Vertex current


def a_search():
    current = grid[start[0], start[1]]
    open_list = []
    closed_list = []

    heapify(open_list)

    while (current != goal): 
        neighbors = get_neighbors(current)
        samePriority = []
        length = len(neighbors)
        for i in range(length):
            cur_neighbor = neighbors[i]
            if ((neighbors[i] not in closed_list) and (neighbors[i] not in open_list)):
                heappush(open_list, (neighbors[i].f_cost, neighbors[i]))

        heapify(open)
                
#c              

#Calculate heuristic distance of start vertex to destination (h)
#Calculate f value for start vertex (f = g + h, where g = 0)
# |WHILE current vertex is not destination
# |  FOR Each vertex adjacent to current
# |  |    IF vertex not in closed list and not in open List THEN
# |  |    |    Add vertex to open list
# |  |    |    Calculate distance from start (g)
# |  |    |    Calculate f value (f = g + h)
# |  |    |   IF new f value < existing f value or there is no existing f value Then
# |  |    |    |    Update f value
# |  |    |    |    Set parent to be current vertex
# |  |    |    END IF 
# |  |    END IF
# |  NEXT adjacent vertex
# |  Add current vertex to closed list
# |  Remove vertex to closed list
# |  Remove vertex with lowest f value from open list and make it current
# |End WHILE   

#Cost from starting node
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

    grid[cell.row][cell.col].g_cost = cell.parent.g_cost + cost 
    

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
