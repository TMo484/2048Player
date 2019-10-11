# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 19:37:10 2018

@author: Tom Mori
"""

from selenium import webdriver

browser = webdriver.Chrome()
url = "https://gabrielecirulli.github.io/2048/"
browser.get(url)