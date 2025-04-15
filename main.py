# import pygame allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Shot.containers = (updateable, drawable, shots)
    AsteroidField.containers = (updateable,)
    Asteroid.containers = (updateable, drawable, asteroids,)
    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable,)
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
    
    dt = 0

    while True:
        # Calculate delta time (time passed since last frame)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")        # Clear the screen and redraw everything

        updateable.update(dt)
        # Update player separately and get new shots
        
        
        for asteroid in asteroids:
            if asteroid.collision(p):
                print("Game over!")
                pygame.quit()       # Quit the game
                return              # Exit the main function    

        for sprite in drawable:     # Draw player
            sprite.draw(screen)
                           
        pygame.display.flip()       # Update the screen
        dt = clock.tick(60) / 1000  # 60 FPS cap, convert to seconds

if __name__ == "__main__":
    main()
