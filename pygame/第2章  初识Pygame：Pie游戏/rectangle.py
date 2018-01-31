#coding:utf-8

# 绘制移动矩形
import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("移动的矩形")

# 当前位置
pos_x = 300
pos_y = 250
# 移动速度
v_x = 0.2
v_y = 0.1

while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()

	screen.fill((0, 0, 200))

	# 移动矩形
	pos_x += v_x
	pos_y += v_y

	# 若到达窗口边缘则反向
	if pos_x > screen.get_width() - 100 or pos_x < 0:
		v_x = -v_x
	if pos_y > screen.get_height() - 100 or pos_y < 0:
		v_y = -v_y

	# 画矩形
	color = 255,255,0
	width = 0
	pos = pos_x, pos_y, 100, 100  # 左上角坐标 + 长宽
	pygame.draw.rect(screen, color, pos, width)

	pygame.display.update()