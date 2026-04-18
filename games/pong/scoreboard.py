import pygame


class Scoreboard:
    def __init__(self, font: pygame.font.Font):
        self.left_score = 0
        self.right_score = 0
        self.font = font

    def l_point(self) -> None:
        self.left_score += 1

    def r_point(self) -> None:
        self.right_score += 1

    def draw(self, surface: pygame.Surface, width: int) -> None:
        left_text = self.font.render(str(self.left_score), True, (255, 255, 255))
        right_text = self.font.render(str(self.right_score), True, (255, 255, 255))

        left_rect = left_text.get_rect(center=(width // 2 - 80, 50))
        right_rect = right_text.get_rect(center=(width // 2 + 80, 50))

        surface.blit(left_text, left_rect)
        surface.blit(right_text, right_rect)
