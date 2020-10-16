import pygame
import math

WIDTH = 700
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Algorithm")

#Defined colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (127, 127, 127)

class Cell:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_position(self):
        return self.row, self.col

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))
        
#BLOCKED_CELL = '0'
#REGULAR_UNBLOCKED_CELL = '1'
#HARD_TO_TRAVERSE_CELL = '2'
#REGULAR_UNBLOCKED_CELL_HIGHWAY = 'a'
#HARD_TO_TRAVERSE_CELL_HIGHWAY = 'b'

def generate_grid(rows, cols, width):
    #(120, 160)
    #arr = [[0 for i in range(cols)] for j in range(rows)]
    grid - []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            cell = Cell(i, j, gap, rows)
            grid[i].append(cell)
def draw_grid(window, rows, cols, width):
    gap = width //rows
    for i in range (rows):
        pygame.draw.line(window, GREY, (0, i * gap), (width, i * gap))
        for j in range (cols):
            pygame.draw.line(window, GREY, (j * gap, 0), (j * gap, width))
def draw(window, grid, rows, width):
    window.fill(WHITE)

    for row
#def generate_start():

#def generate_goal(): 

def generate_map():
    generate_grid()
