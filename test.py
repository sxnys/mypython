#coding:utf-8

import sys
import pygame
from pygame.locals import*

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("移动的圆")

cx = 100
cy = 100
r = 50
vx = 1
vy = 1

while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()

	screen.fill((0, 100, 0))
	color = (0, 0, 200)
	cx = cx + vx
	cy = cy + vy
	if cx <= 0 or cx >= screen.get_width() - r:
		vx = -vx
	if cy <= 0 or cy >= screen.get_height() - r:
		vy = -vy
	width = 5
	c = cx, cy
	pygame.draw.circle(screen, color, c, r, width)
	pygame.display.update()
