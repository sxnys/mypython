# -*- coding: utf-8 -*-

# 对于动态网页，最直接但是可能有时候比想象中困难的抓包，具体怎么抓（有时候真的不那么容易）：
# 分析源代码+审查元素+在network中寻找需要的XHR文件或者相应的js请求地址，大部分情况就是找json

# 以淘宝某店铺卖的pro7评价为例，找到了请求地址，就是json数据地址，解析一下完事

import requests
import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')


url = '''https://rate.tmall.com/list_detail_rate.htm?itemId=556026351191&spuId=862987600&sellerId=1695308781&order=3&current
Page=1&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvIpvWvRhvUvCkvvvvvjiPP2cvQjnmPsz96j1VPmPUgjEbn2spzjrnnLLOtjiPR
phvCvvvvvmCvpvWz2Avc9zNznswSXl4dphvmpvWF9bdTQvgaIwCvvpvCvvvvphvC9vhvvCvpUyCvvOUvvVvayJivpvUvvmvd1NsjAmtvpvIvvvvvhCvvvvvvUn
vphvWRQvv96CvpC29vvm2phCvhhvvvUnvphvppvyCvhQpvzgvCzVYiXVvVE6Fp%2B0x9WkXjLEc6acEKBm6NB3rgjcGe11zp%2FFhARmOV0Q4S47B9Ck%2FPBc
B%2Bb0GVBIG28L%2BkweA%2Bm%2BpFOcnDBvX2QhvCvvvMMGtvpvhvvvvv8wCvvpvvUmm&isg=At7ebKZeC_jH2V8cGgzNodY4L3TgN6Ny-GV6w4hnCCEcq3-F
8CzUKCZN14Fc&needFold=0&_ksTS=1509008138098_670&callback=jsonp671'''

response = requests.get(url)

jsonData = json.loads(response.text.strip()[9:-1])

reviewList = [rev['rateContent'] for rev in jsonData['rateDetail']['rateList']]

for i, r in enumerate(reviewList):
    with open('reviewOfPro7.json', 'a') as f:
        f.write('%d、%s\n\n' % ((i + 1), r))
        f.close()
