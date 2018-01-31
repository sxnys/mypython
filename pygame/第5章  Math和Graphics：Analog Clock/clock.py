# coding: utf-8

import pygame, sys, math, random, time
from datetime import datetime, date, time
from pygame.locals import *

def print_text(font, x, y, text, color = (255, 255, 255)):
	imgText = font.render(text, True, color)
	screen.blit(imgText, (x, y))

def wrap_angle(angle):
	return angle % 360

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("CLOCK")

font = pygame.font.Font('simkai.ttf', 26)
orange = 220, 180, 0
white = 255, 255, 255
yellow = 255, 255, 0
pink = 255, 100, 100
red = 242, 85, 0

pos_x = 500
pos_y = 400
radius = 250
angle = 360

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]:
		sys.exit()

	screen.fill((0, 0, 100))

	# 获取当前时间
	today = datetime.today()
	hours = today.hour % 12
	minutes = today.minute
	seconds = today.second

	# 画表盘
	color = 200, 220, 200
	pygame.draw.circle(screen, color, (pos_x, pos_y), radius + 1, 8)
	
	# 美化的多个同心圆（时分秒对应三个同心圆，对应的时间变化一次，同心圆颜色变换一次）
	hour_circle_color = (today.hour * today.hour + 100) % 255, today.hour + 100, today.hour + 100
	min_circle_color = (today.minute * today.minute + 50) % 255, today.minute * 2 + 100, today.minute + 150
	sec_circle_color = (today.second * today.second + 50) % 255, today.second + 100, today.second + 150
	pygame.draw.circle(screen, sec_circle_color, (pos_x, pos_y), radius - 5, 0)
	pygame.draw.circle(screen, min_circle_color, (pos_x, pos_y), radius - 60, 0)
	pygame.draw.circle(screen, hour_circle_color, (pos_x, pos_y), radius - 140, 0)

	# 画表盘数字
	for n in range(1, 13):
		angle = math.radians(n * (360 / 12) - 90)

		tx = 8
		ty = 10
		# 12和6位置特殊处理一下，更美观（都是细节问题）
		if n == 12:
			tx = 12
		if n == 6:
			tx = 6

		x = math.cos(angle) * (radius - 37) - tx
		y = math.sin(angle) * (radius - 37) - ty
		# if y > 0:
		# 	y -= 25
		print_text(font, pos_x + x, pos_y + y, str(n), (100, 50, 0))

	# 画表盘刻度
	for n in range(1, 61):
		angle = math.radians(n * (360 / 60) - 90)
		x1 = math.cos(angle) * (radius - 5)
		y1 = math.sin(angle) * (radius - 5)
		start = pos_x + x1, pos_y + y1
		l = 8
		w = 3
		if n % 5 == 0:
			l = 16
			w = 6
		end = pos_x + x1 - l * math.cos(angle), pos_y + y1 - l * math.sin(angle)
		color = white
		if n % 15 == 0:
			color = red
		pygame.draw.line(screen, color, start, end, w)


	# 当前时间三针偏离正12点的角度
	sec_angle = seconds * (360 / 60)
	min_angle = minutes * (360 / 60) + seconds / 60.0 * (360 / 60)
	hour_angle = hours * (360 / 12) + minutes / 60.0 * (360 / 12) + seconds / 3600.0 * (360 / 12)

	# 画时针
	hour_angle = wrap_angle(hour_angle - 90)
	hour_angle = math.radians(hour_angle)
	hour_x = math.cos(hour_angle) * (radius - 110)
	hour_y = math.sin(hour_angle) * (radius - 110)
	target = (pos_x + hour_x, pos_y + hour_y)
	pygame.draw.line(screen, pink, (pos_x, pos_y), target, 20)

	# 画分针
	min_angle = wrap_angle(min_angle - 90)
	min_angle = math.radians(min_angle)
	min_x = math.cos(min_angle) * (radius - 90)
	min_y = math.sin(min_angle) * (radius - 90)
	target = (pos_x + min_x, pos_y + min_y)
	pygame.draw.line(screen, orange, (pos_x, pos_y), target, 10)
	
	# 画秒针
	sec_angle = wrap_angle(sec_angle - 90)
	sec_angle = math.radians(sec_angle)
	sec_x = math.cos(sec_angle) * (radius - 70)
	sec_y = math.sin(sec_angle) * (radius - 70)
	target = (pos_x + sec_x, pos_y + sec_y)
	pygame.draw.line(screen, yellow, (pos_x, pos_y), target, 6)

	# 画中心圆
	pygame.draw.circle(screen, white, (pos_x, pos_y), 20)

	print_text(font, 40, 50, '{:02}'.format(today.hour) + ":" + '{:02}'.format(minutes) + 
		":" + '{:02}'.format(seconds))


	pygame.display.update()
