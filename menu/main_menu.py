import pygame

selected_index = 0

buttons = [
    ("Snake", (100, 120, 600, 100)),
    ("Pong", (100, 230, 600, 100)),
    ("Turtle Crossing", (100, 340, 600, 100)),
    ("US States Game", (100, 450, 600, 100)),
]

def run(screen):

    font = pygame.font.Font(None, 48)
    running = True

    while running:
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for text, rect_data in buttons:
            rect = pygame.Rect(rect_data)
            pygame.draw.rect(screen, "white", rect, width=4, border_radius=10)

            text_surface = font.render(text, True, "white")
            text_rect = text_surface.get_rect(center=rect.center)
            screen.blit(text_surface, text_rect)

        pygame.display.flip()