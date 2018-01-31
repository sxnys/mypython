# coding: utf-8

import sys, pygame, random, time, math
from pygame.locals import *

def print_text(font, x, y, text, color = (255, 255, 255)):
	imgText = font.render(text, True, color)
	screen.blit(imgText, (x, y))

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Bomb Catcher Game")

font = pygame.font.Font("Consola.ttf", 24)
font1 = pygame.font.Font("Consola.ttf", 48)

pygame.mouse.set_visible(False)  ###
white = 255, 255, 255
red = 220, 50, 50
yellow = 230, 230, 50
black = 0, 0, 0

lives = 3
score = 0
game_over = True
mouse_x = mouse_y = 0
pos_x = 300
pos_y = 460
bomb_x = random.randint(0, 500)
bomb_y = -50
vel_y = 0.3
start = 0
second = 1
bomb = 0

# 引线
line_c1 = 0
line_c2 = 0
line_c3 = 0

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		elif event.type == MOUSEMOTION:
			mouse_x, mouse_y = event.pos
			move_x, move_y = event.rel
		elif event.type == MOUSEBUTTONUP:
			if game_over:
				game_over = False
				lives = 3
				score = 0

	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]:
		sys.exit()

	screen.fill((0, 0, 100))

	if game_over:
		print_text(font, 200, 200, "<CLICK TO PLAY>")
	else:
		bomb_y += vel_y

		# 是否未抓住球
		if bomb_y > 500:
			if bomb == 0:
				start = time.clock()
			bomb = 1
			print_text(font1, 230, 200, "BOOM!!!")

		# 是否抓住球
		elif bomb_y > pos_y:
			if bomb_x > pos_x and bomb_x < pos_x + 120:
				score += 10
				bomb_x = random.randint(0, 500)
				bomb_y = -50

		current = time.clock() - start
		if bomb == 1 and second - current < 0:
			bomb_x = random.randint(0, 500)
			bomb_y = -50
			bomb = 0
			lives -= 1
			if lives == 0:
				game_over = True

		# 画炸弹
		if bomb == 0:
			pygame.draw.circle(screen, black, (bomb_x - 4, int(bomb_y) - 4), 30, 0)
			pygame.draw.circle(screen, yellow, (bomb_x, int(bomb_y)), 30, 0)
			# 引线
			line_c1 = random.randint(0, 255)
			line_c2 = random.randint(0, 255)
			line_c3 = random.randint(0, 255)
			raduis = 12
			postion1 = bomb_x - raduis / 2, bomb_y - 30 - raduis, raduis, raduis
			postion2 = bomb_x - raduis / 2, bomb_y - 30 - raduis * 2, raduis, raduis
			angle1 = math.radians(90)
			angle2 = math.radians(270)
			angle3 = math.radians(-90)
			color = line_c1, line_c2, line_c3
			pygame.draw.arc(screen, color, postion1, angle1, angle2, 5)
			pygame.draw.arc(screen, color, postion2, angle3, angle1, 5)

		pos_x = mouse_x
		if pos_x < 0:
			pos_x = 0
		elif pos_x > 500:
			pos_x = 500

		# 画挡板
		pygame.draw.rect(screen, black, (pos_x - 4, pos_y - 4, 120, 40), 0)
		pygame.draw.rect(screen, red, (pos_x, pos_y, 120, 40), 0)

	print_text(font, 20, 10, "LIVES: " + str(lives))
	print_text(font, 450, 10, "SCORE: " + str(score))

	pygame.display.update()