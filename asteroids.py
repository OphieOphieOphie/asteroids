import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        vel_one, vel_two, new_rad = self.velocity.rotate(angle), self.velocity.rotate(-angle), self.radius - ASTEROID_MIN_RADIUS
        asteroid_one, asteroid_two = Asteroid(self.position.x, self.position.y, new_rad), Asteroid(self.position.x, self.position.y, new_rad)
        asteroid_one.velocity, asteroid_two.velocity = vel_one * 1.2, vel_two * 1.2