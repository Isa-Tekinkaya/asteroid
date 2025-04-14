from circleshape import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__( x, y, radius)
        self.velocity = pygame.Vector2(1, 0)

    def draw(self, screen):
        # pygame.draw.circle surface, color, center, radius, width
        pygame.draw.circle(screen, "gray", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    