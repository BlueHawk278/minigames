import pygame
import menu.main_menu as menu

import games.pong.main
import games.snake.main
import games.turtle_crossing.main

pygame.init()
pygame.display.set_caption("Minigames")
screen = pygame.display.set_mode((800, 600))

choice = menu.run(screen)

if choice == "snake":
    games.snake.main.run(screen)
if choice == "pong":
    games.pong.main.run(screen)
if choice == "turtle_crossing":
    games.turtle_crossing.main.run(screen)
if choice == "us_states":
    pass

pygame.quit()