import numpy
import cv2


# 通过二维Numpy数组创建一个黑色的正方形图像
img = numpy.zeros((3, 3), dtype=numpy.uint8)
print(img)
print(img.shape)   # 返回图像的结构，即行和列，如果有一个以上的通道还会返回通道数，如BGR格式
# 9个像素，3个列表表示，每个列表3个整数元素，所以一个像素是一个8位无符号整数，像素值0~255


# 将图像转换为BGR格式（Bule-Green-Red）
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print(img)
print(img.shape)  # 三通道
# 9个像素，3个列表表示，每个列表3个列表元素，每个列表元素又有3个整数元素，分别表示B、G、R通道，0~255
