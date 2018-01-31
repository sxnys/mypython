# coding: utf-8

import requests
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://movie.douban.com/top250'

params = {'start': 0}

movie = {
    'name': [],
    'director': [],
    # 'actor': [],
    'year': [],
    'country': [],
    'type': [],
    'quote': [],
}

for i in range(10):
    print u'正在处理第%d页...' % (i + 1)

    params['start'] = i * 25
    response = requests.get(url, params=params)
    response.encoding = 'utf8'
    soup = BeautifulSoup(response.content, 'lxml')

    for mov in soup.find_all('div', class_='info'):
        movie['name'].append(mov.a.span.text.strip())

        some_info = mov.p.text.strip().split('\n')

        movie['director'].append(some_info[0].split(u'主演:')[0].strip(u'导演:').strip())
        # movie['actor'].append(some_info[0].split(u'主演:')[1].strip())
        movie['year'].append(some_info[1].split('/')[0].strip())
        movie['country'].append(some_info[1].split('/')[1].strip())
        movie['type'].append(some_info[1].split('/')[2].strip())

        # print i, mov.a.span.text.strip()
        try:
            movie['quote'].append(mov.find('p', class_='quote').text.strip())
        except:
            movie['quote'].append('(nothing)')

for i in range(len(movie['name'])):
    with open('movie-top250.txt'.decode("gb2312").encode("utf-8"), 'a') as f:
        f.write(u'排名：%d\n' % (i + 1))
        
        f.write(u'电影名：')
        f.write(movie['name'][i] + '\n')

        f.write(u'导演：')
        f.write(movie['director'][i] + '\n')

        # f.write(u'演员：')
        # f.write(movie['actor'][i] + '\n')

        f.write(u'年代：')
        f.write(movie['year'][i] + '\n')

        f.write(u'国家：')
        f.write(movie['country'][i] + '\n')

        f.write(u'类型：')
        f.write(movie['quote'][i] + '\n')

        f.write(u'短评：')
        f.write(movie['name'][i] + '\n\n')

        f.close()
