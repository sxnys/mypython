""" 灰度图像8位，image[0][0] == 255；BGR图像24位，image[0][0] 则是一个三通道列表，表示(0,0)处像素的颜色"""

import cv2
import numpy
import os

# 若图像的每个通道都是8位，则可以转换为标准的一维bytearray格式
# 反之bytearray含有恰当的顺序和字节，也可以显式转换和重构，得到numpy.array形式的图像

# 创建120000个随机字节
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)

# 根据随机字节生成随机400*300的灰度图像
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('randomGray.png', grayImage)

# 根据随机字节生成随机400*100的BGR图像
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('randomColor.png', bgrImage)