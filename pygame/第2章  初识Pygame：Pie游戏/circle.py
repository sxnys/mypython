#coding:utf-8

# 绘制圆 
import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("圆")  # 设置标题

while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	screen.fill((0,0,200))

	color = 255,255,0
	position = 300, 250
	radius = 100
	width = 10		# 若线条宽度是0，则画出来的是该颜色的实心圆
	pygame.draw.circle(screen, color, position, radius, width)

	pygame.display.update()