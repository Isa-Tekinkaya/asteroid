from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=1)

    def update(self, dt):
        self.position += self.velocity * dt