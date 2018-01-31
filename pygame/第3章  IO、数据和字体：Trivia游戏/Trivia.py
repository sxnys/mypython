#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pygame
from pygame.locals import *

class Trivia():
	def __init__(self, filename):
		self.data = []
		self.current = 0
		self.total = 0
		self.correct = 0
		self.score = 0
		self.scored = False
		self.failed = False
		self.wronganswer = 0
		self.colors = [white, white, white, white]

		# 从文本文件中读取数据
		f = open(filename, "r")
		trivia_data = f.readlines()
		f.close()

		for text_line in trivia_data:
			self.data.append(text_line.strip().decode('gbk', 'utf-8'))
			self.total += 1


	# 绘制屏幕（标题、页脚、问题、答案），正确显示绿色
	# 否则显示红色并把正确答案显示绿色
	def show_question(self):
		print_text(font1, width / 2 - fw1 * 2.5, 10, u"计算机网络")
		print_text(font2, width / 2 - fw2 * 5, height - 40, u"（请按A~D选择答案）", purple)
		print_text(font2, width - width / 5, 15 + fw1, u"得分：", purple)
		print_text(font2, width - width / 5 + 3 * fw2 + 5, 15 + fw1, str(self.score), purple)

		# 从数据中得到正确答案（一个问题有4个可选项，接下来是正确答案的序号）
		self.correct = int(self.data[self.current + 5])

		# 显示问题
		question = self.current // 6 + 1
		print_text(font1, 10, fw1 + fw2 + 20 + tmp, u"问题" + str(question))
		print_text(font2, 20, 3 * fw1 + fw2 + 20 + tmp, self.data[self.current], yellow)

		# 显示答案
		print_text(font1, 10, 2 * fw1 + 2 * fw2 + 100 + tmp, u"选项")
		print_text(font2, 20, 2 * fw1 + 3 * fw2 + 140 + tmp, "A、" + self.data[self.current + 1], self.colors[0])
		print_text(font2, 20, 2 * fw1 + 4 * fw2 + 160 + tmp, "B、" + self.data[self.current + 2], self.colors[1])
		print_text(font2, 20, 2 * fw1 + 5 * fw2 + 180 + tmp, "C、" + self.data[self.current + 3], self.colors[2])
		print_text(font2, 20, 2 * fw1 + 6 * fw2 + 200 + tmp, "D、" + self.data[self.current + 4], self.colors[3])

		# 答案正误的不同显示
		if self.scored:
			self.colors = [white, white, white, white]
			self.colors[self.correct - 1] = green
			print_text(font1, width / 2 - fw1 * 2.5, height - fw2 - 80 - fw1 - 20, u"答案正确！", green)
			print_text(font2, width / 2 - fw2 * 5.5, height - fw2 - 80, u"按回车键进入下一个问题", green)
		elif self.failed:
			self.colors = [white, white, white, white]
			self.colors[self.wronganswer - 1] = red
			self.colors[self.correct - 1] = green
			print_text(font1, width / 2 - fw1 * 2.5, height - fw2 - 80 - fw1 - 20, u"答案错误！", red)
			print_text(font2, width / 2 - fw2 * 5.5, height - fw2 - 80, u"按回车键进入下一个问题", red)

	# 响应输入
	def handle_input(self, number):
		if not self.scored and not self.failed:
			if number == self.correct:
				self.scored = True
				self.score += 1
			else:
				self.failed = True
				self.wronganswer = number

	# 继续下一个问题
	def next_question(self):
		if self.scored or self.failed:
			self.scored = False
			self.failed = False
			self.correct = 0
			self.colors = [white, white, white, white]
			self.current += 6

	# 题目全做完了
	def finish_all(self):
		print_text(font1, width / 2 - fw1 * 13, height / 2 - fw1,
					u"题目全部做完了，您的最终得分为" + str(self.score) + "，是否选择重做（Y/N）")

# 打印文本
def print_text(font, x, y, text, color = (255, 255, 255), shadow = True):
	if shadow:
		imgText = font.render(text, True, (0, 0, 0))
		screen.blit(imgText, (x - 2, y - 2))
	imgText = font.render(text, True, color)
	screen.blit(imgText, (x, y))


# 主代码
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("选择题")

fw1 = 40
fw2 = 24
font1 = pygame.font.Font('./simkai.ttf', fw1)
font2 = pygame.font.Font('./simkai.ttf', fw2)

tmp = 50  # 整体移动的大小，可变

width = screen.get_width()
height = screen.get_height()

white = 255, 255, 255
cyan = 0, 255, 255
yellow = 255, 255, 0
purple = 255, 0, 255
green = 0, 255, 0
red = 255, 0, 0

trivia = Trivia("1.txt")

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		
		elif event.type == KEYUP:
			if event.key == pygame.K_ESCAPE:
				sys.exit()

			elif event.key == pygame.K_a:
				trivia.handle_input(1)
			elif event.key == pygame.K_b:
				trivia.handle_input(2)
			elif event.key == pygame.K_c:
				trivia.handle_input(3)
			elif event.key == pygame.K_d:
				trivia.handle_input(4)

			elif event.key == pygame.K_RETURN:
				trivia.next_question()

			# 选择是否重做
			elif trivia.current >= trivia.total:
				if event.key == pygame.K_y:
					trivia.current = 0
					trivia.score = 0
				elif event.key == pygame.K_n:
					sys.exit()

	screen.fill((0, 0, 200))
	# 根据是否到达最后一题作不同的操作
	if trivia.current >= trivia.total:
		trivia.finish_all()
	else:
		trivia.show_question()
	pygame.display.update()
