import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_BLACK, COLOR_WHITE, PADDLE_WIDTH, PADDLE_HEIGHT, BALL_SIZE
from src.paddle import Paddle
from src.ball import Ball

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.running = True

        # Initialize paddles and ball
        self.paddle1 = Paddle(30, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle2 = Paddle(SCREEN_WIDTH - 30 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_SIZE)

    def handle_input(self):
        keys = pygame.key.get_pressed()

        # Paddle 1 controls
        if keys[pygame.K_w]:
            self.paddle1.speed = -0.5
        elif keys[pygame.K_s]:
            self.paddle1.speed = 0.5
        else:
            self.paddle1.speed = 0

        # Paddle 2 controls
        if keys[pygame.K_UP]:
            self.paddle2.speed = -0.5
        elif keys[pygame.K_DOWN]:
            self.paddle2.speed = 0.5
        else:
            self.paddle2.speed = 0

    def run(self):
        while self.running:
            delta_time = self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_input()

            # Update game objects
            self.paddle1.move(delta_time)
            self.paddle2.move(delta_time)
            self.ball.move(delta_time)

            # Constrain paddles
            self.paddle1.constrain(SCREEN_HEIGHT)
            self.paddle2.constrain(SCREEN_HEIGHT)

            # Ball collision and reset
            if self.ball.check_bounds(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.ball.reset(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

            self.ball.handle_collision(self.paddle1)
            self.ball.handle_collision(self.paddle2)

            # Render objects
            self.screen.fill(COLOR_BLACK)
            self.paddle1.draw(self.screen, COLOR_WHITE)
            self.paddle2.draw(self.screen, COLOR_WHITE)
            self.ball.draw(self.screen, COLOR_WHITE)

            pygame.display.flip()

        pygame.quit()
