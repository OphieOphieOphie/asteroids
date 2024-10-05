import pygame
import random
from constants import *
from circleshape import CircleShape
from vector_math import final_velocities

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
        angle = random.uniform(30,60)
        vel_one, vel_two, new_rad = self.velocity.rotate(angle), self.velocity.rotate(-angle), self.radius - ASTEROID_MIN_RADIUS

        offset = new_rad * 1.7

        a_1_pos, a_2_pos = self.position + vel_one.normalize() * offset, self.position + vel_two.normalize() * offset

        asteroid_one, asteroid_two = Asteroid(a_1_pos.x, a_1_pos.y, new_rad), Asteroid(a_2_pos.x, a_2_pos.y, new_rad)
        asteroid_one.velocity, asteroid_two.velocity = vel_one * 1.2, vel_two * 1.2

    def bounce(self, other):
        vel_one, vel_two = final_velocities(self.velocity, other.velocity, self.position, other.position, self.radius**3, other.radius**3)
        self.velocity.x, self.velocity.y = vel_one[0] * 1.0004, vel_one[1] * 1.0004
        other.velocity.x, other.velocity.y = vel_two[0] * 1.0004, vel_two[1] * 1.0004