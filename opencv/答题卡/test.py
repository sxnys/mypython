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
rotated = cv2.warpAffine(thresh, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

# cv2.imshow('rotated', rotated)
# cv2.waitKey()
# cv2.destroyAllWindows()
cv2.imwrite('rotated.jpg', rotated)

