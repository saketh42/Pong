import pygame
import random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)


def main():

    # Initialize the PyGame library
    pygame.init()

    # Create the window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Customising the window
    pygame.display.set_caption("Pong")

    # Game loop
    while True:
        screen.fill(COLOR_BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    if __name__ == "__main__":
        main()




