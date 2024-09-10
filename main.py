# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    # this sets up the window size of the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    '''
     # Game loop, it has 3 functions -
     1. To take input from user. Say, go left or right key strokes
     2. Update the game world based on the inputs (basically update the backend)
     3. Draw the game based on the updates onto the screen
    '''
    
    while(True):
        # this allows the window that opens up to have the close button enabled
        for event in pygame.event.get():
            # if we click on close, we can exit
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()