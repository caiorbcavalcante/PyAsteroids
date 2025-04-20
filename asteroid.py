from player import *
import random
from circleshape import CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Parent class will set position and radius

    def draw(self, screen):
        # Use the already defined position and radius
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            # Split the asteroid into two smaller asteroids
            self.kill()  # Remove the current asteroid
            new_radius = self.radius / 2
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            # Set random velocities for the new asteroids
            speed = random.randint(40, 100)
            angle1 = random.randint(-30, 30)
            angle2 = random.randint(30, 90)
            new_asteroid1.velocity = pygame.Vector2(speed, 0).rotate(angle1)
            new_asteroid2.velocity = pygame.Vector2(speed, 0).rotate(angle2)
            
            return [new_asteroid1, new_asteroid2]
        else:
            self.kill()  # Remove the current asteroid if it's too small

