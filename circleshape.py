import pygame
from constants import *

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

    def collision(self, other):
        # Check if the two circles are colliding
        distance  = self.position.distance_to(other.position)
        distance -= self.radius + other.radius
        return distance <= 0
    
class Shot(CircleShape):
    def __init__(self, x, y):
        # Use the SHOT_RADIUS constant from your constants file
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)  # Set initial velocity to zero
    
    def draw(self, screen):
        # Draw a bullet (typically a small white circle)
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)
    
    def update(self, dt):
        # Update the shot's position based on its velocity
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt