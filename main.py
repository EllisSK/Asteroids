import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    
    player0 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    a_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")       
        updateable.update(dt)
        for d_item in drawable:
            d_item.draw(screen)

        for a_item in asteroids:
            if a_item.collision_check(player0):
                print("Game over!")
                sys.exit(0)
            for s_item in shots:
                if a_item.collision_check(s_item):
                    a_item.kill()
                    s_item.kill()

        pygame.display.flip()        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
