from constants import *
import pygame

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # Set the frame rate to 60 FPS
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # Exit the game
        dt = clock.tick(60) / 1000 # Convert milliseconds to seconds
            
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()