# coding: utf-8
# Pygame事件
# QUIT
# ACTIVEEVENT
# KEYDOWN
# KEYUP
# MOUSEMOTION
# MOUSEBUTTONUP
# MOUSEBUTTONDOWN
# JOYAXISMOTION
# JOYBALLMOTION
# JOYHATMOTION
# JOYBUTTONUP
# JOYBUTTONDOWN
# VIDEORESIZE
# VIDEOEXPOSE
# USEREVENT

while True:		# 实时事件循环
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

		# 键盘事件
		elif event.type == KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
		# 重复响应一个持续被按下的键
		# pygame.key.set_repeat(10)
		# 参数以毫秒为单位

		# 鼠标事件
		# MOUSEMOTION 属性 event.pos, event.rel, event.buttons
		elif event.type == MOUSEMOTION:
			mouse_x, mouse_y = event.pos
			move_x, move_y = event.rel
		# MOUSEBUTTONDOWN, MOUSEBUTTONUP 属性 event.pos, event.buttons
		elif event.type == MOUSEBUTTONDOWN:
			mouse_down = event.button
			mouse_down_x, mouse_down_y = event.pos
		elif event.type == MOUSEBUTTONUP:
			mouse_up = event.button
			mouse_up_x, mouse_up_y = event.pos
