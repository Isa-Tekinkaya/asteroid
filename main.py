# import pygame allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from player import Player
def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    pygame.init()
    clock = pygame.time.Clock()
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Calculate delta time (time passed since last frame)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Clear the screen and redraw everything
        screen.fill("black")
        updateable.update(dt)  # Update player with the correct delta time
        for sprite in drawable:  # Draw player
            sprite.draw(screen)
                               

        pygame.display.flip() # Update the screen
        dt = clock.tick(60) / 1000  # 60 FPS cap, convert to seconds

if __name__ == "__main__":
    main()
