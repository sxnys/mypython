"""
根据文本进行图像倾斜矫正
"""
import numpy as np
import cv2

# 加载图片，将它转换为灰阶
img = cv2.imread('initial.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

# 二值化，将图片黑白色反转
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# 得到旋转角度
coords = np.column_stack(np.where(thresh > 0))
angle = cv2.minAreaRect(coords)[-1]
angle = -(90 + angle) if angle < -45 else -angle

print(angle)

# 执行仿射变换对倾斜角度校正
h, w = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
rotatedGary = cv2.warpAffine(thresh, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

cv2.imwrite('Rotated.jpg', rotated)
cv2.imwrite('RotatedGary.jpg', rotatedGary)


''' 计算指定区域内平均灰度 '''
def aveGray(grayimg, x, y, w, h):
	sumGray = sum(grayimg[j, i] for j in range(y+1, y+h) for i in range(x+1, x+w))
	return sumGray // ((w - 1) * (h - 1))


''' 在所有边缘检测的结果中找出需要的矩形部分 '''
def detectRect(img, grayimg, imgName='', width=30, threshold=200, sortkey=0):
	# 边缘检测，会有很多很多奇奇怪怪的轮廓
	image, contours, hierarchy = cv2.findContours(grayimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	posBlock = list()
	# 将所有轮廓用矩形框出，大于一定宽度并且区域内灰度平均值大于阈值的，就是需要的定位块或者填涂块
	for c in contours:
		x, y, w, h = cv2.boundingRect(c)
		if w > width and aveGray(grayimg, x, y, w, h) > threshold:
			cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
			posBlock.append((x, y, w, h))
			# print(aveGray(grayimg, x, y, w, h))
	# 保存相应的灰度图像和带矩形标记的BGR图
	cv2.imwrite('{}.jpg'.format(imgName), grayimg)
	cv2.imwrite('contours{}.jpg'.format(imgName), img)
	return sorted(posBlock, key=lambda pb: pb[sortkey])


height, width = rotatedGary.shape

# 截取答题卡顶部部分区域寻找试卷大定位块
cropTop = rotated[:height//10, :]
cropTopGray = rotatedGary[:height//10, :]
largePosBlock = detectRect(cropTop, cropTopGray, 'CropTop', 100, 190)

# 根据大定位块，截取答题卡左右两侧寻找试卷题目定位块, 必须len(largePosBlock) == 2
left_crop_width = 100
left_base_x = largePosBlock[0][0]
sl = slice(left_base_x - left_crop_width, left_base_x)
cropLeft = rotated[:, sl]
cropLeftGray = rotatedGary[:, sl]
leftPosBlock = detectRect(cropLeft, cropLeftGray, 'CropLeft', 30, 190, 1)

right_base_x = largePosBlock[1][0] + largePosBlock[1][2]
cropRight = rotated[:, right_base_x : ]
cropRightGray = rotatedGary[:, right_base_x : ]
rightPosBlock = detectRect(cropRight, cropRightGray, 'CropRight', 30, 190, 1)


print(len(leftPosBlock), len(rightPosBlock))

''' 客观题 '''
row, col, num = 6, 4, 23
answer = dict.fromkeys(range(1, num + 1))
answerDict = dict(zip(range(1, 5), 'A B C D'.split()))
# 确定一对定位块之间题目的填涂答案
# 观察图片，以选项间空白的一半为一个单位，划分如下：
# 每个题目（包括题号）占20个单位（题号、选项每个都是占4个单位），第二第三题之间的空白占4个单位，图片首末各占1个单位
# 一共86个单位
def getAnswer(width, questionRect, row_no):
	unit = width // 86
	# 一行题目所有可涂选项的区域范围（横向），这里一行4题，一共有16个元素
	options = [(unit*i, unit*(i+4)) for i in range(1, 86 - 1, 4) if i not in [1, 1+5*4, 1+10*4, 1+11*4, 1+16*4]]

	for qr in questionRect:
		mid_x = (qr[0] + qr[0] + qr[2]) // 2    # 填涂区域的中心横向位置 (x + (x + w)) / 2
		for i, op in enumerate(options):
			if op[0] < mid_x < op[1]:
				answer[(row_no - 1) * col + i // 4 + 1] = answerDict.get(i % 4 + 1)



# 根据题目定位块和指定的题目行列数截取每一行题目，如果一对定位块上下位置相差过大则抛出异常
# if max(ly+lh, ry+rh) - min(ly, ry) > max(lh, rh) + 20:
# 	raise SomeError()
for i in range(row):
	lx, ly, lw, lh = leftPosBlock[i]
	rx, ry, rw, rh = rightPosBlock[i]
	start = left_base_x - (left_crop_width - (lx + lw))
	end = right_base_x + rx
	sl = slice(min(ly, ry)-10, max(ly+lh, ry+rh)+10)
	cropQuestion = rotated[sl, start:end]
	cropQuestionGray = rotatedGary[sl, start:end]

	# 所有正确填涂的答案位置 (x, y, w, h)，阈值是127
	questionRect = detectRect(cropQuestion, cropQuestionGray, 'CropQuestion%s'%(i+1), 40, 127)
	
	getAnswer(cropQuestion.shape[1], questionRect, i + 1)

print(answer)
