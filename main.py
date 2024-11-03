# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
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

    # group for asteroids and players
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # group of shots
    shots = pygame.sprite.Group()
    # group of all asteroids
    asteroids = pygame.sprite.Group()
    # all containers
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
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

        # player.update(dt)
        for updatables in updatable:
            updatables.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if(asteroid.is_colliding(player)):
                sys.exit("Game Over!")
            # Check if bullet hits any asteroid
            for shot in shots:
                if (shot.is_colliding(asteroid)):
                    # print("Previous asteroid count:", len(asteroids))
                    asteroid.split()
                    shot.kill() # kill is built in method of pygame, removes objects from all its groups, hence object would stop drawing
                    # print("After asteroid count:", len(asteroids))
            
        screen.fill("black")
        # player.draw(screen)
        for drawables in drawable:
            drawables.draw(screen)

        # renders the screen
        pygame.display.flip()
        # It pauses the gameloop until 1/60th time has passed (Framerate to 60 FPS)
        dt = clock.tick(60) / 1000 # milliseconds to seconds
if __name__ == "__main__":
    main()