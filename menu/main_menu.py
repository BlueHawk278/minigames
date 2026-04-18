import pygame

selected_index = 0

buttons = [
    ("Snake", (100, 120, 600, 100), "snake"),
    ("Pong", (100, 230, 600, 100), "pong"),
    ("Turtle Crossing", (100, 340, 600, 100), "turtle_crossing"),
    ("US States Game", (100, 450, 600, 100), "us_states"),
]

def run(screen):
    font = pygame.font.Font(None, 48)
    clock = pygame.time.Clock()
    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for _, rect_data, game_key in buttons:
                    rect = pygame.Rect(rect_data)
                    if rect.collidepoint(mouse_pos):
                        return game_key

        for text, rect_data, _ in buttons:
            rect = pygame.Rect(rect_data)
            hovered = rect.collidepoint(mouse_pos)

            border_color = "yellow" if hovered else "white"
            text_color = "yellow" if hovered else "white"

            pygame.draw.rect(screen, border_color, rect, width=4, border_radius=10)

            text_surface = font.render(text, True, text_color)
            text_rect = text_surface.get_rect(center=rect.center)
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)