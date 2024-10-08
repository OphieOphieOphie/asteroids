import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN
import shot

class Player(CircleShape):
    def __init__(self, x, y, radius = PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.cooldown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.cooldown -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * (dt)
        self.pos_adjust()

    def shoot(self):
        if self.cooldown <= 0:
            new_shot = shot.Shot(self.position, self.rotation)
            self.cooldown = PLAYER_SHOOT_COOLDOWN