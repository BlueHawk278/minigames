import pygame


class Scoreboard:
    def __init__(self):
        self.level = 1
        self.font = pygame.font.Font(None, 38)

    def increase_level(self):
        self.level += 1

    def draw(self, surface: pygame.Surface):
        txt = self.font.render(f"Level: {self.level}", True, (255, 255, 255))
        surface.blit(txt, (20, 20))

    def draw_game_over(self, surface: pygame.Surface, width: int, height: int):
        over = self.font.render("GAME OVER", True, (255, 80, 80))
        hint = pygame.font.Font(None, 32).render("Press R to retry or ESC for menu", True, (220, 220, 220))
        surface.blit(over, over.get_rect(center=(width // 2, height // 2 - 20)))
        surface.blit(hint, hint.get_rect(center=(width // 2, height // 2 + 20)))
