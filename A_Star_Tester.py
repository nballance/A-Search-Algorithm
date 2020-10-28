from Map import *
# from Draw_Grid import *
from Heuristic_Search2 import a_search_standard, a_search, calculate_f_val, calculate_g_val, uniform_search, distance, calculate_h_val
# from Heuristic_Search import *

class Cell:
    def __init__(self, row, col, terrain, g_cost, h_cost, f_cost, parent):
        self.row = row
        self.col = col
        self.terrain = terrain
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = f_cost
        self.parent = parent

# def make_grid():
#     for column in range (COLS):
#         grid.append([])
#         for row in range(ROWS):
#             grid[column].append(Cell(column, row, '1', -1, -1, -1, None))

def main():
    #RUN THE ALGORITHM HERE
    #THE SMALLER GRID WILL 
    #ALLOW YOU TO TRACK NUMBERS
    #YOU CAN SET TERRAIN VALUES MANUALLY

    #E.G. grid[1][2].terrain = 'a'
    #make sure that river to river counts by not river to non-river
    make_grid()
    # make_start()
    # make_goal()
    start = (0, 0)

    goal = (6, 3)
    print(start, goal)

    
    grid[0][0].terrain = '1'
    grid[1][0].terrain = '1'
    grid[2][0].terrain = 'a'
    grid[3][0].terrain = '1'
    grid[4][0].terrain = '0'
    grid[5][0].terrain = '0'
    grid[6][0].terrain = '0'

    grid[0][1].terrain = '1'
    grid[1][1].terrain = '1'
    grid[2][1].terrain = 'a'
    grid[3][1].terrain = '1'
    grid[4][1].terrain = '0'
    grid[5][1].terrain = '0'
    grid[6][1].terrain = '0'

    grid[0][2].terrain = '0'
    grid[1][2].terrain = '1'
    grid[2][2].terrain = 'a'
    grid[3][2].terrain = '0'
    grid[4][2].terrain = '2'
    grid[5][2].terrain = '2'
    grid[6][2].terrain = '0'

    grid[0][3].terrain = '0'
    grid[1][3].terrain = '0'
    grid[2][3].terrain = 'a'
    grid[3][3].terrain = '1'
    grid[4][3].terrain = '2'
    grid[5][3].terrain = '2'
    grid[6][3].terrain = '1'
    

    # neighbors = get_neighbors(3, 1)

    # print("row ", grid[3][1].row, "col ", grid[3][1].col)
    
    # print("Row: ", neighbors[0].row, "Col: ", neighbors[0].col)
    # print(neighbors[1])
    # print(neighbors[2])
    # print(neighbors[3])
    # print(neighbors[4])
    
    
    
    # draw_grid()

    # print(a_search_standard())

    a_search_standard()
    
    # print(grid[6][3].g_cost)

    print_grid()

if __name__ == "__main__":
    main()
