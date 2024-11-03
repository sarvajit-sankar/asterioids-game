import pygame

# Base class for game objects
'''
# this is used so that every object even if not a circle
#  is represented internally as circle, 
# so that we can easily calculate collision between 2 objects in our game
'''

# base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding(self, other):
        distance_between_objects = self.position.distance_to(other.position)
        # distance between 2 objects <= r1 + r2
        return distance_between_objects <= self.radius + other.radius