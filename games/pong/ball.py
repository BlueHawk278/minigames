import pygame


class Ball:
    def __init__(self, x: int, y: int, radius: int = 10):
        self.start_x = x
        self.start_y = y
        self.radius = radius
        self.reset(to_right=True)

    def reset(self, to_right: bool = True) -> None:
        self.x = float(self.start_x)
        self.y = float(self.start_y)
        self.vx = 360.0 if to_right else -360.0
        self.vy = 230.0

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(int(self.x - self.radius), int(self.y - self.radius), self.radius * 2, self.radius * 2)

    def update(self, dt: float) -> None:
        self.x += self.vx * dt
        self.y += self.vy * dt

    def bounce_y(self) -> None:
        self.vy *= -1

    def bounce_x(self) -> None:
        self.vx *= -1
        self.vx *= 1.03
        self.vy *= 1.03

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), self.radius)