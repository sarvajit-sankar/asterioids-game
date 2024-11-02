import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # draws onto the screen a white triangle
    def draw(self, screen):
        # line width is taken as 2
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # updates the rotation of the player based on the key pressed
    def update(self, dt):
        keys = pygame.key.get_pressed()
        # if left key(a) is pressed
        if keys[pygame.K_a]:
            self.rotate(-dt)
        # if right key(d) is pressed
        if keys[pygame.K_d]:
            self.rotate(dt)
        #if up key(w) is pressed
        if keys[pygame.K_w]:
            self.move(dt)
        #if down key(s) is pressed
        if keys[pygame.K_s]:
            self.move(-dt)

    # updates the position of the player            
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
