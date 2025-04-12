# import pygame allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from player import Player
def main():
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        # Calculate delta time (time passed since last frame)
        dt = clock.tick(60) / 1000  # 60 FPS cap, convert to seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Clear the screen and redraw everything
        screen.fill("black")
        p.update(dt)  # Update player with the correct delta time
        p.draw(screen)  # Draw player

        pygame.display.flip() # Update the screen
        
if __name__ == "__main__":
    main()
