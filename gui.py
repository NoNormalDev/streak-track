import pygame
pygame.init()
from sys import exit
import random
import colorsys
import math
import json
import os

def rnd(x: int|float) -> int:
    return math.floor(x+0.5)

bgcolorhsv = [random.randint(0,100)/100,0.5,0.5]
bgcolorrgb = list(colorsys.hsv_to_rgb(bgcolorhsv[0],bgcolorhsv[1],bgcolorhsv[2]))
for i in range(3):
    bgcolorrgb[i] = rnd(bgcolorrgb[i]*100)
bgcolor = pygame.Color(bgcolorrgb[0],bgcolorrgb[1],bgcolorrgb[2])

screenInfo = pygame.display.Info()
screenW = screenInfo.current_w
screenH = screenInfo.current_h

windowH = screenH * (2/3)
windowW = windowH * (7/12)

screen = pygame.display.set_mode((windowW,windowH),pygame.RESIZABLE)
pygame.display.set_caption("Streak Track")

clock = pygame.time.Clock()
fpsgoal = 60
fpsgoaltime = 1/fpsgoal

class IO:
    @staticmethod
    def read() -> list:
        ex = IO.exists()
        if not ex:
            return []
        f = open("data.json","r",encoding="utf8")
        rtr = json.loads(f.read())
        f.close()
        return rtr
    @staticmethod
    def write(inp:list) -> None:
        f = open("data.json","w",encoding="utf8")
        f.write(json.dumps(inp))
        f.close()
    @staticmethod
    def exists() -> bool:
        return os.path.exists("data.json")

data = []
data = IO.read()
for d in data:
    print(d)

while True:
    if not pygame.event.get(pygame.QUIT) == []:
        pygame.quit()
        exit()

    screen.fill(bgcolor)

    pygame.display.update()
    
    currentfps = clock.get_fps()
    if currentfps == 0:
        newfps = fpsgoal
    else:
        currenttime = 1/currentfps
        newtime = fpsgoaltime + (fpsgoaltime-currenttime)
        newfps = 1/newtime
    clock.tick(newfps)