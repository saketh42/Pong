import pygame
import random

class Ball:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.speed_x = random.choice([-0.3, 0.3])
        self.speed_y = random.choice([-0.3, 0.3])

    def move(self, delta_time):
        self.rect.x += self.speed_x * delta_time
        self.rect.y += self.speed_y * delta_time

    def check_bounds(self, screen_width, screen_height):
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            return True  # Ball is out of bounds
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1
        return False

    def handle_collision(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.speed_x *= -1

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.choice([-0.3, 0.3])
        self.speed_y = random.choice([-0.3, 0.3])

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)
