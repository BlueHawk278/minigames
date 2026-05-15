import random
import pygame


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.refresh()

    def refresh(self):
        possible_x = range(-400, 400, 20)
        possible_y = range(-300, 300, 20)
        self.position = (random.choice(possible_x), random.choice(possible_y))

    def draw(self, surface: pygame.Surface, center_x: int, center_y: int):
        x, y = self.position
        sx = center_x + x - 8
        sy = center_y + y - 8
        pygame.draw.rect(surface, (50, 150, 255), (sx, sy, 16, 16), border_radius=4)
