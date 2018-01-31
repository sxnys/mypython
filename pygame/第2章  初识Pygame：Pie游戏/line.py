#coding:utf-8

# 绘制线段
import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("线段")

while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()

	screen.fill((0, 80, 0))
	color = 100, 255, 200
	width = 8
	pygame.draw.line(screen, color, (100, 100), (500, 400), width)
	pygame.display.update()