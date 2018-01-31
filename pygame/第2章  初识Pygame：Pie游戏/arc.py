#coding:utf-8

# 画弧形
import sys
import math
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("弧形")

while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()

	screen.fill((0, 0, 200))
	color = 255, 0, 255
	postion = 0, 0, 200, 200  # 边界矩形, 左上角 + 长宽
	width = 8
	start_angle = math.radians(0)  # 角度换弧度
	end_angle = math.radians(180)
	pygame.draw.arc(screen, color, postion, start_angle, end_angle, width)
	pygame.display.update()