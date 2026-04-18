import pygame

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self):
        self.segments = []
        self.direction = RIGHT
        self.create_snake()

    @property
    def head(self):
        return self.segments[0]

    def create_snake(self):
        self.segments = list(STARTING_POSITIONS)
        self.direction = RIGHT

    def extend(self):
        self.segments.append(self.segments[-1])

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i] = self.segments[i - 1]

        hx, hy = self.head
        dx, dy = self.direction
        self.segments[0] = (hx + dx * MOVE_DISTANCE, hy + dy * MOVE_DISTANCE)

    def reset_snake(self):
        self.create_snake()

    def kill(self):
        self.segments.clear()

    def up(self):
        if self.direction != DOWN:
            self.direction = UP

    def down(self):
        if self.direction != UP:
            self.direction = DOWN

    def left(self):
        if self.direction != RIGHT:
            self.direction = LEFT

    def right(self):
        if self.direction != LEFT:
            self.direction = RIGHT

    def draw(self, surface: pygame.Surface, center_x: int, center_y: int):
        for x, y in self.segments:
            sx = center_x + x - 10
            sy = center_y + y - 10
            pygame.draw.rect(surface, (255, 255, 255), (sx, sy, 20, 20), border_radius=3)
