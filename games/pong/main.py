import pygame

from .paddle import Paddle
from .ball import Ball
from .scoreboard import Scoreboard


def run(screen: pygame.Surface):
    clock = pygame.time.Clock()
    width, height = screen.get_size()

    paddle_w = 20
    paddle_h = 100
    padding = 40

    l_paddle = Paddle(padding, height // 2 - paddle_h // 2, paddle_w, paddle_h)
    r_paddle = Paddle(width - padding - paddle_w, height // 2 - paddle_h // 2, paddle_w, paddle_h)

    ball = Ball(width // 2, height // 2)
    font = pygame.font.Font(None, 64)
    small_font = pygame.font.Font(None, 36)
    scoreboard = Scoreboard(font)

    # States: "start_menu", "playing", "score_pause"
    state = "start_menu"
    score_pause_until = 0  # pygame time in ms when pause ends

    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        now = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"

                # Start from Pong menu
                if state == "start_menu" and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    state = "playing"

        keys = pygame.key.get_pressed()

        # Allow paddle movement during gameplay and score pause
        # (feels responsive while waiting for next serve)
        if state in ("playing", "score_pause"):
            if keys[pygame.K_w]:
                l_paddle.move_up(dt)
            if keys[pygame.K_s]:
                l_paddle.move_down(dt)
            if keys[pygame.K_UP]:
                r_paddle.move_up(dt)
            if keys[pygame.K_DOWN]:
                r_paddle.move_down(dt)

            l_paddle.clamp(height)
            r_paddle.clamp(height)

        if state == "playing":
            ball.update(dt)

            # Wall collision
            if ball.y - ball.radius <= 0 or ball.y + ball.radius >= height:
                ball.bounce_y()

            # Paddle collision
            if ball.rect.colliderect(l_paddle.rect) and ball.vx < 0:
                ball.x = l_paddle.rect.right + ball.radius
                ball.bounce_x()

            if ball.rect.colliderect(r_paddle.rect) and ball.vx > 0:
                ball.x = r_paddle.rect.left - ball.radius
                ball.bounce_x()

            # Miss / score -> pause before next serve
            if ball.x - ball.radius > width:
                scoreboard.l_point()
                ball.reset(to_right=False)
                state = "score_pause"
                score_pause_until = now + 2000  # 2 seconds

            if ball.x + ball.radius < 0:
                scoreboard.r_point()
                ball.reset(to_right=True)
                state = "score_pause"
                score_pause_until = now + 2000  # 2 seconds

        elif state == "score_pause":
            if now >= score_pause_until:
                state = "playing"

        # Draw
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (100, 100, 100), (width // 2, 0), (width // 2, height), 2)

        l_paddle.draw(screen)
        r_paddle.draw(screen)
        ball.draw(screen)
        scoreboard.draw(screen, width)

        if state == "start_menu":
            title = font.render("PONG", True, (255, 255, 255))
            prompt = small_font.render("Press SPACE or ENTER to start", True, (220, 220, 220))
            back = small_font.render("Press ESC to return to menu", True, (180, 180, 180))

            screen.blit(title, title.get_rect(center=(width // 2, height // 2 - 60)))
            screen.blit(prompt, prompt.get_rect(center=(width // 2, height // 2)))
            screen.blit(back, back.get_rect(center=(width // 2, height // 2 + 40)))

        elif state == "score_pause":
            pause_text = small_font.render("Point scored! Next serve in 2...", True, (220, 220, 220))
            screen.blit(pause_text, pause_text.get_rect(center=(width // 2, height // 2)))

        pygame.display.flip()

    return "menu"