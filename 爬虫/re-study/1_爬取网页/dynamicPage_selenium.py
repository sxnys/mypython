# -*- coding: utf-8 -*-

# 不需要GUI的话用PhantomJS驱动，而且它是最快速高效的，需要GUI的话用一些主流浏览器驱动，但是需要另外下载驱动，
# 如火狐需要geckodriver，Chrome需要chromedriver

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
