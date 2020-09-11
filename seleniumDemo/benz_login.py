# -*- coding:utf-8 -*-

from selenium import webdriver
import time

n = 2
driver = webdriver.Chrome()
driver.get('https://benzthtest.bluepay.asia/login?moduleName=login')
print(driver.title, driver.current_url)

driver.find_element_by_xpath('//input[@id="inspire"]/div/main/div/div/div[2]/div/form/div[1]/div/div[1]/div/input').clear()
driver.find_element_by_xpath('')
driver.find_element_by_xpath('//*[@id="inspire"]/div/main/div/div/div[2]/div/form/div[1]/div/div[1]/div/input').send_keys('test')