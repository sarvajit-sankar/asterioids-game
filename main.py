# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from constants import *

def main():
    pygame.init()
    # this sets up the window size of the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initializing FPS
    clock = pygame.time.Clock()
    # delta time - amount of time since last frame was drawn
    dt = 0
    '''
     # Game loop, it has 3 functions -
     1. To take input from user. Say, go left or right key strokes
     2. Update the game world based on the inputs (basically update the backend)
     3. Draw the game based on the updates onto the screen
    '''
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while(True):
        # this allows the window that opens up to have the close button enabled
        for event in pygame.event.get():
            # if we click on close, we can exit
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # player.draw(screen)
        for drawables in drawable:
            drawables.draw(screen)
        # player.update(dt)
        for updatables in updatable:
            # 60 FPS - It pauses the gameloop until 1/60th sec has passed
            dt = clock.tick(60)
            dt = dt / 1000 # milliseconds to seconds
            updatables.update(dt)
        
        # renders the screen
        pygame.display.flip()
if __name__ == "__main__":
    main()