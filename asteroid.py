import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, MAX_ASTEROID_SPLIT_ANGLE, MIN_ASTEROID_SPLIT_ANGLE


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position +=  self.velocity * dt
    
    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return # this was smallest asteroid, hence, no smaller asteroids to create
        else:
            angle = random.uniform(MIN_ASTEROID_SPLIT_ANGLE, MAX_ASTEROID_SPLIT_ANGLE)
            left_asteroid_velocity = self.velocity.rotate(-angle)
            right_asteroid_velocity = self.velocity.rotate(angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            left_asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            # making new asteroids which are smaller to move faster than old
            left_asteroid.velocity = left_asteroid_velocity * 1.2
            right_asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            right_asteroid.velocity = right_asteroid_velocity * 1.2