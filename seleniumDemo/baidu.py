# -*- coding:utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
print(driver.title)
# driver.find_element_by_id("kw").click()
# driver.find_element_by_name("wd").click()
# driver.find_element_by_class_name("s_ipt").click()
# driver.find_element_by_tag_name("input").click()
# driver.find_element_by_xpath('//*[@id="kw"]').click()
# driver.find_element_by_link_text("新闻").click()
driver.find_element_by_xpath('//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]').click()
print(driver.current_url)
driver.quit()
