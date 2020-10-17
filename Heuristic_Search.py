#TODO: Needed to implement make__
# def distance(x_1, y_1, x_2, y_2):
#   Method to find the distance from one cell to another cell
#    print() 
from heapq import heapify, heappush, heappop
from Map import *

#Initialize open and closed lists
#Make the start Vertex current

current = start
open_list = []
closed_list = []

heapify(open_list)


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
#






def distance():
    pass

