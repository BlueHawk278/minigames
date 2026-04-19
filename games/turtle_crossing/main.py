import pygame

from .player import Player
from .car_manager import CarManager
from .scoreboard import Scoreboard


def run(screen: pygame.Surface):
    clock = pygame.time.Clock()
    width, height = screen.get_size()

    player = Player(width // 2 - 11, height - 50)
    cars = CarManager(width, height)
    scoreboard = Scoreboard()

    state = "start"

    while True:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"

                if state == "start" and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    state = "playing"

                elif state == "playing" and event.key in (pygame.K_UP, pygame.K_w):
                    player.move_up()

                elif state == "game_over" and event.key == pygame.K_r:
                    player = Player(width // 2 - 11, height - 50)
                    cars = CarManager(width, height)
                    scoreboard = Scoreboard()
                    state = "start"

        if state == "playing":
            cars.update(dt)

            for car_rect, _ in cars.cars:
                if player.rect.colliderect(car_rect):
                    state = "game_over"
                    break

            if player.rect.top <= 0:
                player.reset_position()
                cars.increase_speed()
                scoreboard.increase_level()

        screen.fill((20, 20, 20))
        pygame.draw.rect(screen, (40, 120, 40), (0, 0, width, 45))
        pygame.draw.rect(screen, (40, 120, 40), (0, height - 45, width, 45))

        cars.draw(screen)
        player.draw(screen)
        scoreboard.draw(screen)

        if state == "start":
            title = pygame.font.Font(None, 64).render("Turtle Crossing", True, (255, 255, 255))
            hint = pygame.font.Font(None, 34).render("Press SPACE or ENTER to start", True, (220, 220, 220))
            esc = pygame.font.Font(None, 30).render("Press ESC to return to menu", True, (180, 180, 180))
            screen.blit(title, title.get_rect(center=(width // 2, height // 2 - 40)))
            screen.blit(hint, hint.get_rect(center=(width // 2, height // 2 + 5)))
            screen.blit(esc, esc.get_rect(center=(width // 2, height // 2 + 36)))

        elif state == "game_over":
            scoreboard.draw_game_over(screen, width, height)

        pygame.display.flip()
