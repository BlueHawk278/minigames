import os
import pygame
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, "50_states.csv")
MAP_FILE = os.path.join(BASE_DIR, "blank_states_img.gif")
OUTPUT_FILE = os.path.join(BASE_DIR, "states_to_learn.csv")

def run(screen):
    data = pd.read_csv(DATA_FILE)
    all_states = data["state"].tolist()
    guessed_states = []

    map_img = pygame.image.load(MAP_FILE).convert()
    width, height = map_img.get_width(), map_img.get_height()

    font = pygame.font.SysFont("arial", 20)
    small_font = pygame.font.SysFont("arial", 16)
    clock = pygame.time.Clock()

    user_text = ""
    running = True

    while running and len(guessed_states) < 50:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user_text = "Exit"
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    answer_state = user_text.strip().title()
                    user_text = ""

                    if answer_state == "Exit":
                        missing_states = [s for s in all_states if s not in guessed_states]
                        pd.DataFrame(missing_states).to_csv(OUTPUT_FILE)
                        running = False
                    elif answer_state in all_states and answer_state not in guessed_states:
                        guessed_states.append(answer_state)

                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    if event.unicode.isprintable():
                        user_text += event.unicode

        screen.fill((255, 255, 255))

        map_x = (screen.get_width() - width) // 2
        map_y = (screen.get_height() - height) // 2
        screen.blit(map_img, (map_x, map_y))

        for state in guessed_states:
            row = data[data.state == state].iloc[0]
            x, y = int(row.x), int(row.y)

            px = width // 2 + x
            py = height // 2 - y

            text_surface = small_font.render(state, True, (0, 0, 0))
            screen.blit(text_surface, (map_x + px, map_y + py))

        title = font.render(f"{len(guessed_states)}/50 States Correct", True, (0, 0, 0))
        prompt = small_font.render("Type a state and press Enter (or type Exit)", True, (0, 0, 0))
        typed = small_font.render(user_text, True, (20, 20, 20))

        screen.blit(title, (10, 10))
        screen.blit(prompt, (10, 35))
        pygame.draw.rect(screen, (255, 255, 255), (10, 55, 380, 24))
        pygame.draw.rect(screen, (0, 0, 0), (10, 55, 380, 24), 1)
        screen.blit(typed, (14, 59))

        pygame.display.flip()
        clock.tick(60)
