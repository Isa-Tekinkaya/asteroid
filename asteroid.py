from circleshape import *
from constants import *
import pygame
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__( x, y, radius)
        self.velocity = pygame.Vector2(1, 0)

    def draw(self, screen):
        # pygame.draw.circle surface, color, center, radius, width
        pygame.draw.circle(screen, "gray", self.position, self.radius, width=2)

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(angle)
        vector_two = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_one.velocity *= 1.2
        new_asteroid_two.velocity *= 1.2
        new_asteroid_one.velocity = vector_one
        new_asteroid_two.velocity = vector_two

    def update(self, dt):
        self.position += self.velocity * dt
    