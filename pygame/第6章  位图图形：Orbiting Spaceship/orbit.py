# coding: utf-8

import pygame, random, math
from pygame.locals import *

# 点类
class Point(object):
	def __init__(self, x, y):
		self._x = x
		self._y = y

	# X
	def getx(self):
		return self._x
	def setx(self, x):
		self._x = x
	x = property(getx, setx)

	# Y
	def gety(self):
		return self._y
	def sety(self, y):
		self._y = y
	y = property(gety, sety)
	
	def __str__(self):
		return "{X:" + "{:.0f}".format(self._x) + \
			",Y:" + "{:.0f}".format(self._y) + "}"


def print_text(font, x, y, text, color = (255, 255, 255)):
	imgText = font.render(text, True, color)
	screen.blit(imgText, (x, y))

def wrap_angle(angle):
	return angle % 360


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Orbit")
font = pygame.font.Font(None, 18)

# 加载位图
space = pygame.image.load("space.png").convert_alpha()
planet = pygame.image.load("planet.png").convert_alpha()
ship = pygame.image.load("freelance.png").convert_alpha()
width, height = ship.get_size()
# 平滑缩放
ship = pygame.transform.smoothscale(ship, (width / 2, height / 2))

radius = 250		# 飞船移动的轨迹圆的半径
angle = 0.0
pos = Point(0, 0)
old_pos = Point(0, 0)
speed = 0.1

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

		# 变速
		elif event.type == KEYDOWN:
			if event.key == pygame.K_KP_PLUS and speed < 5:
				speed += 0.1
			elif event.key == pygame.K_KP_MINUS and speed > 0.1:
				speed -= 0.1
			
	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]:
		sys.exit()

	# 画背景
	screen.blit(space, (0, 0))

	# 画星球
	width, height = planet.get_size()
	screen.blit(planet, (400 - width / 2, 300 - height / 2))

	# 飞船移动
	angle = wrap_angle(angle - speed)
	pos.x = math.sin(math.radians(angle)) * radius
	pos.y = math.cos(math.radians(angle)) * radius

	# 飞船旋转 ############################################
	delta_x = pos.x - old_pos.x
	delta_y = pos.y - old_pos.y
	rangle = math.atan2(delta_y, delta_x)
	rangled = wrap_angle(-math.degrees(rangle))
	scratch_ship = pygame.transform.rotate(ship, rangled)
	#######################################################

	# 画飞船
	width, height = scratch_ship.get_size()
	x = 400 + pos.x - width / 2
	y = 300 + pos.y - height / 2
	screen.blit(scratch_ship, (x, y))

	# 位置参数的显示
	print_text(font, 0, 0, "Orbit: " + "{:.0f}".format(angle))
	print_text(font, 0, 20, "Rotation: " + "{:.2f}".format(rangle))
	print_text(font, 0, 40, "Postion: " + str(pos))
	print_text(font, 0, 60, "Old Postion: " + str(old_pos))
	print_text(font, 0, 80, "Speed: " + str(speed))

	old_pos.x = pos.x
	old_pos.y = pos.y

	pygame.display.update()