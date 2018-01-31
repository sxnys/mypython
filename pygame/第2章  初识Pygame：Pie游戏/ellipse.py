# coding:utf-8

import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("椭圆")

while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	screen.fill((0, 0, 200))

	color = 0, 100, 0
	rect = 100, 150, 400, 200  # 椭圆的外接矩形, 左上角坐标 + 长宽

	pygame.draw.ellipse(screen, color, rect, 2)
	pygame.display.update()

