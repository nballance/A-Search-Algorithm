import pygame
from Map import *
# Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (173,216,230)

# Screen dimensions
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 950
 
 
class Player(pygame.sprite.Sprite):
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # the "player"
        width = 0
        height = 0
        self.image = pygame.Surface([width, height])
        
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.map = None
 
    def update(self):
        """ Move the player. """
        
        # Move left/right
        self.rect.x += self.change_x
 
        # Move up/down
        self.rect.y += self.change_y
    
        
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -20
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 20

    def go_up(self):
        self.change_y = -20
    
    def go_down(self):
        self.change_y = 20
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.change_y = 0
 

class Block(pygame.sprite.Sprite):
    def __init__(self, width, height, terrain_color):
        super().__init__()
 
        self.image = pygame.Surface([width, height])

        self.image.fill(terrain_color)
 
        self.rect = self.image.get_rect()

        
 
class Map():
    
    def __init__(self, player):
        self.block_list = pygame.sprite.Group()
        self.player = player
 
        self.world_shift_x = 0
        self.world_shift_y = 0

    # Update everythign on this map
    def update(self):
        self.block_list.update()
        
    def draw(self, screen):
    
        # Draw the background
        screen.fill(BLUE)
 
        # Draw all the sprite lists that we have
        self.block_list.draw(screen)
 
    def shift_world(self, shift_x, shift_y):
       
        # Keep track of the shift amount
        self.world_shift_x += shift_x
        self.world_shift_y += shift_y
 
        # Go through all the sprite lists and shift
        for block in self.block_list:
            block.rect.x += shift_x
            block.rect.y += shift_y
        
 
def cell_color(x, y, draw_path):
    if draw_path:
        for coordinate in paths:
            if ((coordinate[0] == x and coordinate[1] == y) and (cell_color(x,y,False) != GREEN) and (cell_color(x,y,False) != RED)):
                # draw_path = True
                return YELLOW
                # break
            # else:
            #     draw_path = False
    # if draw_path == True:
    #     old_color = cell_color(x, y, False) 
    #     return YELLOW
    if x == start[0] and y == start[1]:
        return GREEN
    elif x == goal[0] and y == goal[1]:
        return RED
    terrain = grid[x][y].terrain
    if terrain == '1':
        return WHITE
    elif terrain == '0':
        return BLACK
    elif terrain == '2':
        return GRAY
    else:
        if terrain == 'a':
            return LIGHT_BLUE
        elif terrain == 'b':
            return BLUE

class current_map(Map):
    """ Definition for level 1. """
    
    def __init__(self, player, draw_path, screen):
        """ Create level 1. """
 
        # Call the parent constructor
        Map.__init__(self, player)
 
        
        
        cell_width = 8
        cell_height = 8

        for row in range(ROWS):
            for col in range(COLS):
                block = Block(cell_width, cell_height, cell_color(col, row, draw_path))
                block.rect.x = cell_width * col
                block.rect.y = cell_height * row
                block.player = self.player
                # line = pygame.Surface((cell_width, cell_height))
                # pygame.draw.line(line, RED, (0, 0), (ROWS*COLS, ROWS*COLS), 5)
                self.block_list.add(block)
            
 
 
def draw_grid(draw_path):
    """ Main Program """
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Title")
 
    # Create the player
    player = Player()
 
    map_to_draw = current_map(player, draw_path, screen)
 
    active_sprite_list = pygame.sprite.Group()
    player.map = map_to_draw
 
    player.rect.x = 400
    player.rect.y = 400
    active_sprite_list.add(player)
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    player.go_down()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_UP and player.change_y < 0:
                    player.stop()
                if event.key == pygame.K_DOWN and player.change_y > 0:
                    player.stop()
 
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the map
        map_to_draw.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if (player.rect.right >= 400):
            diff = player.rect.right - 400
            player.rect.right = 400
            map_to_draw.shift_world(-diff, 0)
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 400:
            diff = 400 - player.rect.left
            player.rect.left = 400
            map_to_draw.shift_world(diff, 0)


        if player.rect.top >= 300:
            diff = player.rect.top - 300
            player.rect.top = 300
            map_to_draw.shift_world(0, -diff)
 
        if player.rect.top <= 300:
            diff = 300 - player.rect.top
            player.rect.top = 300
            map_to_draw.shift_world(0, diff)

             

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        map_to_draw.draw(screen)
        active_sprite_list.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 30 frames per second
        clock.tick(30)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    pygame.quit()
 
