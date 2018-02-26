from aip import AipOcr
import requests, json,configure,time,os,base64
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
# 访问百度
driver.get('http://www.baidu.com')

count = 0
screenpath = configure.image_directory
while True:
    text = input('按下回车发起搜索')
    start = time.time()
    count = count + 1
    imagepath = configure.image_directory + "screen" + str(count) + ".png"
    region_path = configure.image_directory + "region" + str(count) + ".png"

    if not os.path.exists(configure.image_directory):
        os.mkdir(configure.image_directory)
    os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png")
    os.system("adb pull /sdcard/screenshot.png " + imagepath)

    im = Image.open(imagepath)
    img_size = im.size
    w = im.size[0]
    h = im.size[1]

    region = im.crop((configure.left, configure.top, w - configure.right, configure.bottom))  # 裁剪的区域
    region.save(region_path)

    f = open(region_path, 'rb')
    ls_f = base64.b64encode(f.read())
    f.close()
    image_byte = bytes.decode(ls_f)


    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=24.84f82283b755b372feb54775e48228ab.2592000.1519214620.282335-10692813'

    data = {
        "image": image_byte,
        "language_type": "CHN_ENG",
        "detect_direction": "false",
        "detect_language": "false",
        "probability": "false"

    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = requests.post(url, data, headers=header)

    content = res.text
    json_data = json.loads(content)['words_result']
    ques = ""
    for i in json_data:
        ques += i['words']

    # ques = ''.join(i['words'] for i in json_data)

    keyword = str(ques).strip().rstrip().lstrip().replace("\r", "").replace("\n","").replace(" ","").replace("不","")

    print(keyword)

    driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id('kw').send_keys(keyword)
    driver.find_element_by_id('su').send_keys(Keys.ENTER)

    end = time.time()
    print('程序用时：' + str(end - start) + '秒')

