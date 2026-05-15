import pygame

from .Snake import Snake
from .Food import Food
from .Scoreboard import Scoreboard


def run(screen: pygame.Surface):
    clock = pygame.time.Clock()
    width, height = screen.get_size()
    center_x, center_y = width // 2, height // 2

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    move_timer = 0.0
    move_interval = 0.1
    game_started = False

    while True:
        dt = clock.tick(60) / 1000.0
        move_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"
                if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    game_started = True
                if event.key in (pygame.K_UP, pygame.K_w):
                    snake.up()
                if event.key in (pygame.K_DOWN, pygame.K_s):
                    snake.down()
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    snake.left()
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    snake.right()

        if game_started and move_timer >= move_interval:
            move_timer = 0.0
            snake.move()

            if snake.head == food.position:
                food.refresh()
                snake.extend()
                scoreboard.increase_score()

            hx, hy = snake.head
            if hx > 400 or hx < -400 or hy > 300 or hy < -300:
                snake.reset_snake()
                scoreboard.reset()
                game_started = False

            for segment in snake.segments[1:]:
                if snake.head == segment:
                    snake.reset_snake()
                    scoreboard.reset()
                    game_started = False
                    break

        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (center_x - 400, center_y - 300), (center_x + 400, center_y - 300), 2)

        snake.draw(screen, center_x, center_y)
        food.draw(screen, center_x, center_y)
        scoreboard.draw(screen, width)

        if not game_started:
            hint_font = pygame.font.Font(None, 34)
            hint = hint_font.render("Press SPACE or ENTER to start", True, (200, 200, 200))
            back = hint_font.render("Press ESC to return to menu", True, (170, 170, 170))
            screen.blit(hint, hint.get_rect(center=(center_x, center_y)))
            screen.blit(back, back.get_rect(center=(center_x, center_y + 36)))

        pygame.display.flip()
