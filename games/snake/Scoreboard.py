from pathlib import Path
import pygame


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score_path = Path(__file__).with_name("High_Score.txt")
        self.high_score = self._load_high_score()
        self.font = pygame.font.Font(None, 36)

    def _load_high_score(self) -> int:
        if not self.high_score_path.exists():
            return 0
        content = self.high_score_path.read_text(encoding="utf-8").strip()
        return int(content) if content else 0

    def _save_high_score(self):
        self.high_score_path.write_text(str(self.high_score), encoding="utf-8")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()
        self.score = 0

    def increase_score(self):
        self.score += 1

    def draw(self, surface: pygame.Surface, width: int):
        text = self.font.render(
            f"Score: {self.score}   High Score: {self.high_score}",
            True,
            (255, 255, 255),
        )
        rect = text.get_rect(center=(width // 2, 24))
        surface.blit(text, rect)
