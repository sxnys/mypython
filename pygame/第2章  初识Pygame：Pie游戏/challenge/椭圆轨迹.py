# coding:utf-8

import sys
import pygame
import math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("椭圆轨迹")

# 焦点坐标
c1 = (200, 250)
c2 = (400, 250)

# 以很小的矩形作为描绘椭圆的点
# 确定矩形的起始位置、颜色和变化量
posx = 300 - math.sqrt(20000)
posy = 250
color = 0, 0, 0
vx = 1

while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	screen.fill((0, 0, 200))

	# 描述轨迹
	posx += vx
	if posx >= 300 + math.sqrt(20000):
		vx = -vx
		posx += vx
	if posx <= 300 - math.sqrt(20000):
		vx = -vx
		posx += vx

	if vx > 0:
		posy = 250 + math.sqrt(10000 - (posx - 300) * (posx - 300) / 2)
	else:
		posy = 250 - math.sqrt(10000 - (posx - 300) * (posx - 300) / 2)


	# 轨迹显示椭圆
	pygame.draw.rect(screen, color, (posx, posy, 5, 5), 5)
	pygame.display.update()
