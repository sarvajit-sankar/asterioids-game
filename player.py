import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
    
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
        if keys[pygame.K_SPACE]:
            self.shoot()
        # decreasing shoot timer everyime update is called by dt(1/1000 seconds)
        self.shoot_timer -= dt

    # updates the position of the player            
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    # shoots bullets
    def shoot(self):
        if self.shoot_timer > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        vector = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = vector * PLAYER_SHOOT_SPEED
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
