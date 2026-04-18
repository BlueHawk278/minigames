import pygame


class Paddle:
    def __init__(self, x: int, y: int, width: int = 20, height: int = 100, speed: int = 420):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move_up(self, dt: float):
        self.rect.y -= int(self.speed * dt)

    def move_down(self, dt: float):
        self.rect.y += int(self.speed * dt)

    def clamp(self, screen_height: int):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect, border_radius=6)
