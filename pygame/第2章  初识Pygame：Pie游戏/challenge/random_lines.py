# coding:utf-8

import sys
import pygame
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("随机1000条直线")

screen.fill((0, 0, 200))

color = 255, 255, 255
width = 1
for i in range(1000):
	start = random.randint(0, 1500), random.randint(0, 1000)
	end = random.randint(0, 1500), random.randint(0, 1000)
	pygame.draw.line(screen, color, start, end, width)
pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()