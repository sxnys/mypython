# coding:utf-8

import sys
import pygame
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("移动变色的矩形")

# 矩形初始左上角坐标
posx = 400
posy = 300

# 移动向量
vx = 0.1
vy = 0.2

kx = 1
ky = 1

# 长宽
l = 100
w = 100

# random color
c1 = 0
c2 = 0
c3 = 0

while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	screen.fill((0, 0, 200))

	posx += vx
	posy += vy

	# 随机速度
	vx = kx * random.randint(0, 10) / 10
	vy = ky * random.randint(0, 10) / 10

	# 速度和颜色变换，速度变换要注意！！！
	if posx <= 0 - vx or posx >= screen.get_width() - l - vx:
		kx = -kx
		c1 = random.randint(0, 255)
		c2 = random.randint(0, 255)
		c3 = random.randint(0, 255)

	if posy <= 0 - vy or posy >= screen.get_height() - w - vy:
		ky = -ky
		c1 = random.randint(0, 255)
		c2 = random.randint(0, 255)
		c3 = random.randint(0, 255)

	color = c1, c2, c3
	width = 5

	pygame.draw.rect(screen, color, (posx, posy, l, w), width)
	pygame.display.update()