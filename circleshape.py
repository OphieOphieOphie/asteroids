import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
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

    def pos_adjust(self):
        if not 0 <= self.position[0] <= SCREEN_WIDTH or not 0 <= self.position[1] <= SCREEN_HEIGHT:
            self.position[0], self.position[1] = self.position[0] % SCREEN_WIDTH, self.position[1] % SCREEN_HEIGHT