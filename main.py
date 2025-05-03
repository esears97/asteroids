# this allows us to use code from
# the open-source pygame library
# throughout the file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        screen.fill("black")
        time_passed = game_clock.tick(60)
        dt = time_passed / 1000
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()
