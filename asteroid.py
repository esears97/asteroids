from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        direction1 = self.velocity.rotate(angle)
        direction2 = self.velocity.rotate(-angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        pygame.Vector2()
        ast1 = Asteroid(self.position.x, self.position.y, new_rad)
        ast1.velocity = direction1 * 1.2
        ast2 = Asteroid(self.position.x, self.position.y, new_rad)
        ast2.velocity = direction2 * 1.2

