import cv2
import os
from PIL import Image, ImageDraw, ImageFont

ascii_char = list('MNHQ$OC67+>!:-. ')

# 将像素转换为ascii码
def get_char(r, g, b, alpha=256):
	if alpha == 0:
		return ''
	length = len(ascii_char)
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	unit = (256.0 + 1) / length
	return ascii_char[int(gray / unit)]

# 将txt转换为图片
def txt2image(file_name):

	im = Image.open(file_name).convert('RGB')

	raw_width = im.width
	raw_height = im.height
	width = int(raw_width/6)
	height = int(raw_height/15)
	im = im.resize((width, height), Image.NEAREST)

	txt = ''
	colors =[]
	for i in range(height):
		for j in range(width):
			pixel = im.getpixel((j,i))
			colors.append((pixel[0], pixel[1], pixel[2]))
			if len(pixel) == 4:
				txt += get_char(pixel[0], pixel[1], pixel[2], pixel[3])
			else:
				txt += get_char(pixel[0], pixel[1], pixel[2]) 
		txt += '\n'
		colors.append((255, 255, 255))
	# if file_name == '1.jpg':
	# 	print(txt)
	im_txt = Image.new('RGB', (raw_width, raw_height), (255,255,255)) 
	dr = ImageDraw.Draw(im_txt)
	font = ImageFont.load_default().font
	x = y = 0
	font_w, font_h = font.getsize(txt[1])
	font_h *= 1.37

	for i in range(len(txt)):
		if txt[i] == '\n':
			x += font_h
			y = -font_w
		dr.text([y, x], txt[i], colors[i])
		y += font_w

	im_txt.save(file_name)

# 将视频解析成图片
def video_to_pic(file_name):
	vc = cv2.VideoCapture(file_name)
	FPS = vc.get(cv2.CAP_PROP_FPS)
	c = 1
	if vc.isOpened():
		r, frame = vc.read()  # 读取第一帧视频
		if not os.path.exists('Cache'):
			os.mkdir('Cache')
		os.chdir('Cache')
	else:
		r = False
	while r:
		cv2.imwrite(str(c) + '.jpg', frame)
		txt2image(str(c) + '.jpg')  # 转ascii图
		r, frame = vc.read()
		c += 1
	os.chdir('..')
	vc.release()  # 释放资源
	return FPS

# 将图片合成视频
def pic_to_video(fps):  # 参数为帧率
	fourcc = cv2.VideoWriter_fourcc(*'XVID')

	images = os.listdir('Cache')
	# print(images)
	im = Image.open('Cache/' + images[0])
	vm = cv2.VideoWriter('output.mp4', fourcc, fps, im.size)  # 初始化视频

	os.chdir('Cache')
	for image in sorted(images, key=lambda x: int(x.split('.')[0]))[1:]:
		frame = cv2.imread(image)
		vm.write(frame)
	os.chdir('..')
	vm.release()


if __name__ == '__main__':
	fps = video_to_pic('lige.mp4')
	pic_to_video(fps)