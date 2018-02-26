from aip import AipOcr


APP_ID = '10692813'
API_KEY = 'BcQZQFEKEkeDNClOGFCeAVK8'
SECRET_KEY = 'rohsjK0ApKlmWvst175fyPVokaCw5SSG'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

image_directory = "D:/screenshots/"
driver_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

# left = 30 # 距离左边的像素
# top = 400 # 距离顶部的像素         350
# right = 30 # 距离右边的像素
# bottom = 800 #距离顶部的像素       600

# DDD
left = 50 # 距离左边的像素
top = 300 # 距离顶部的像素
right = 50 # 距离右边的像素
bottom = 800 #距离顶部的像素

# #youku
# left = 50 # 距离左边的像素
# top = 360 # 距离顶部的像素         350
# right = 50 # 距离右边的像素
# bottom = 630 #距离顶部的像素       600
