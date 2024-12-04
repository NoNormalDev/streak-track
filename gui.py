import pygame
from sys import exit

pygame.init()

screenInfo = pygame.display.Info()
screenW = screenInfo.current_w
screenH = screenInfo.current_h

windowH = screenH * (2/3)
windowW = windowH * (7/12)

screen = pygame.display.set_mode((windowW,windowH),pygame.RESIZABLE)
pygame.display.set_caption("Streak Track")

while True:
    if not pygame.event.get(pygame.QUIT) == []:
        pygame.quit()
        exit()
    