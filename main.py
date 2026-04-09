import pygame
import menu.main_menu as menu

pygame.init()
pygame.display.set_caption("Minigames")
screen = pygame.display.set_mode((800, 600))
menu.run(screen)
pygame.quit()