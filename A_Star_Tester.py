COLS = 4
ROWS = 4

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

def main():
    #RUN THE ALGORITHM HERE
    #THE SMALLER GRID WILL 
    #ALLOW YOU TO TRACK NUMBERS
    #YOU CAN SET TERRAIN VALUES MANUALLY

    #E.G. grid[1][2].terrain = 'a'
    #make sure that river to river counts by not river to non-river
    
    print()
if __name__ == "__main__":
    main()
