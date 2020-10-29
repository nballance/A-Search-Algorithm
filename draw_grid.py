import pygame
from Map import *
# Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (212, 212, 212)
BLUE = (0, 0, 255)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
 
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
    
        # See if we are on the ground.
        # if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
        #     self.change_y = 0
        #     self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    
 
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
    """ Platform the user can jump on """
 
    def __init__(self, width, height, terrain):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(terrain)
 
        self.rect = self.image.get_rect()

        # self.rect_with_border = self.rect.copy()
        # pygame.draw.rect(rect_with_border, (255, 0, 0), (0, 0, 47, 47), 2)
        
 
class Map():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.block_list = pygame.sprite.Group()
        self.player = player
 
        self.world_shift_x = 0
        self.world_shift_y = 0

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.block_list.update()
        
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        screen.fill(BLUE)
 
        # Draw all the sprite lists that we have
        self.block_list.draw(screen)
 
    def shift_world(self, shift_x, shift_y):
        """ When the user moves left/right and we need to scroll
        everything: """
 
        # Keep track of the shift amount
        self.world_shift_x += shift_x
        self.world_shift_y += shift_y
 
        # Go through all the sprite lists and shift
        for block in self.block_list:
            block.rect.x += shift_x
            block.rect.y += shift_y
        
 
def cell_color(x, y):
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
        return BLUE

class current_map(Map):
    """ Definition for level 1. """
    
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Map.__init__(self, player)
 
        
        
        cell_width = 20
        cell_height = 20

        # Go through the array above and add platforms
        for row in range(ROWS):
            for col in range(COLS):
                block = Block(cell_width, cell_height, cell_color(col, row))
                block.rect.x = cell_width * col
                block.rect.y = cell_height * row
                block.player = self.player
                self.block_list.add(block)
            
 
 
def draw_grid():
    """ Main Program """
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Title")
 
    # Create the player
    player = Player()
 
    map_to_draw = current_map(player)
 
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
 
        # Update items in the level
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
 
        # Limit to 60 frames per second
        clock.tick(30)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
