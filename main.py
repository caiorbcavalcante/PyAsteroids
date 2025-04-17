from constants import *
from player import Player
import pygame

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2
player = Player(x, y)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # Set the frame rate to 60 FPS
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.container = (updatable,drawable)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # Exit the game
        dt = clock.tick(60) / 1000 # Convert milliseconds to seconds
            
        screen.fill("black")
        updatable.update(dt)
        drawable.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()