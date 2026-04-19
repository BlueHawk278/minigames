import random
import pygame

class CarManager:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.cars = []
        self.car_speed = 220
        self.spawn_timer = 0.0
        self.spawn_interval = 0.45

    def increase_speed(self):
        self.car_speed += 20

    def update(self, dt: float):
        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0.0
            car_h = 26
            car_w = random.randint(45, 75)
            y = random.randint(60, self.height - 60)
            rect = pygame.Rect(self.width + car_w, y, car_w, car_h)
            color = (
                random.randint(80, 255),
                random.randint(80, 255),
                random.randint(80, 255),
            )
            self.cars.append((rect, color))

        updated = []
        for rect, color in self.cars:
            rect.x -= int(self.car_speed * dt)
            if rect.right > 0:
                updated.append((rect, color))
        self.cars = updated

    def draw(self, surface: pygame.Surface):
        for rect, color in self.cars:
            pygame.draw.rect(surface, color, rect, border_radius=6)
