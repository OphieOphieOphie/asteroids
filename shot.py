import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, player_pos, player_rot, radius = SHOT_RADIUS):
        super().__init__(player_pos.x, player_pos.y, radius)
        self.position = player_pos.copy()
        self.rotation = pygame.Vector2(0, 1).rotate(player_rot)
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += SHOT_SPEED * dt * self.rotation