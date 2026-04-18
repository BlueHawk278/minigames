import pygame
import games.pong.main
import menu.main_menu as menu

pygame.init()
pygame.display.set_caption("Minigames")
screen = pygame.display.set_mode((800, 600))

choice = menu.run(screen)

if choice == "snake":
    pass
if choice == "pong":
    games.pong.main.run(screen)
if choice == "turtle_crossing":
    pass
if choice == "us_states":
    pass

pygame.quit()