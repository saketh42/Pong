import pygame

class Paddle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 0

    def move(self, delta_time):
        self.rect.y += self.speed * delta_time

    def constrain(self, screen_height):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)
