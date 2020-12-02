# _*_ coding: utf-8 _*_
# @Time : 2020/12/1 16:56 

# @Author : youding

# @File : test.py

# @Software: PyCharm Community Edition

from selenium import webdriver
import sys
c_path = "d:\\project\\AutoLab\\bin"
sys.path.append(c_path)
c = c_path + '\\chromedriver.exe'

dr = webdriver.Chrome(executable_path=c)
dr.get('http://www.baidu.com')
dr.close()