import cv2

# 加载图片，将它转换为灰阶，轻度模糊，然后边缘检测。
image = cv2.imread('testimg.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# edged = cv2.Canny(blurred, 75, 200)

# cv2.imwrite('testimg1.jpg', edged)

ret, thresh = cv2.threshold(image, 127, 255, 0)
img, contours, *rest = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
image = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
cv2.imshow('contours', color)
cv2.waitKey()
cv2.destroyAllWindows()