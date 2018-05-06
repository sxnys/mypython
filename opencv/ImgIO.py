import cv2

# 加载图像并转换为灰度图像（即会丢失所有的颜色信息）
grayImg = cv2.imread('testread.png', cv2.IMREAD_GRAYSCALE)  # 第二项为可选参数，还有其它的
# 保存图像为JPEG格式
cv2.imwrite('testwirte.jpg', grayImg)

print(grayImg.item(0, 0))
print(grayImg[0, 0])
