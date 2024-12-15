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

    # Paddles
    paddle_1_rect = pygame.Rect(30, 0, 7, 100)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)

    # Paddle Movement
    paddle_1_move = 0
    paddle_2_move = 0

    # Ball rectangle
    ball_rect = pygame.Rect(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 25, 25)

    # Ball speed
    ball_accel_x = random.randint(2, 4) * 0.1
    ball_accel_y = random.randint(2, 4) * 0.1

    # Ball direction
    if random.randint(1, 2) == 1:
        ball_accel_x *= -1
    if random.randint(1, 2) == 1:
        ball_accel_y *= -1

    # Clock to keep track of time
    clock = pygame.time.Clock()

    # Flag for Game starting
    started = False

    # Game loop
    while True:
        # Fill BG Black
        screen.fill(COLOR_BLACK)

        # Make ball move
        if not started:
            font = pygame.font.SysFont('Consolas', 30)

            # Text on the center of the screen
            text = font.render("Press Space to Start...", True, COLOR_WHITE)
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_HEIGHT//2, SCREEN_HEIGHT//2)
            screen.blit(text, text_rect)

            # Update the display
            pygame.display.flip()

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        started = True

        for event in pygame.event.get():
            # Exit condition
            if event.type == pygame.QUIT:
                return

        # Display Player 1 and Player 2
        pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)
    
        # Display Ball
        pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

        # Display update
        pygame.display.update()
        delta_time = clock.tick(60)

        

    if __name__ == "__main__":
        main()
main()


