#coding:utf-8

import pygame
import sys
from pygame.locals import *

# 初始化
pygame.init()
# 指定分辨率的窗口
screen = pygame.display.set_mode((600, 500))
# 创建字体对象
myfont = pygame.font.Font("myfont.ttf", 60)
# 文本渲染
white = 255,255,255
blue = 0,0,255
textImage = myfont.render("Hello Pygame", True, white) # 文本，抗锯齿字体标志，颜色RGB

while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN): # 监听是否存在关闭或按下任意键的操作
			sys.exit()
	screen.fill(blue)
	screen.blit(textImage, (100, 100))  # 绘制函数
	pygame.display.update()  # 刷新显示