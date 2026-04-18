import pygame


class Player:
    def __init__(self, start_x: int, start_y: int):
        self.width = 22
        self.height = 22
        self.start_x = start_x
        self.start_y = start_y
        self.rect = pygame.Rect(start_x, start_y, self.width, self.height)
        self.move_step = 25

    def move_up(self):
        self.rect.y -= self.move_step

    def reset_position(self):
        self.rect.topleft = (self.start_x, self.start_y)

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (50, 220, 100), self.rect, border_radius=6)
