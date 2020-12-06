# -*- coding:utf-8 -*-

from selenium import webdriver
import time


n = 1
# 驱动文件路径
# driverfile_path = r"C:\Program Files (x86)\Google\Chrome\Application"
# driver = webdriver.Chrome(executable_path=driverfile_path)
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
print(driver.title, driver.current_url)
assert '百度一下，你就知道' in driver.title, '没找到该元素'

# driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(n)

# driver.find_element_by_name("wd").click()
# driver.find_element_by_class_name("s_ipt").click()
# driver.find_element_by_tag_name("input").click()
driver.find_element_by_partial_link_text("中央").click()
# driver.find_element_by_css_selector()
# driver.find_element_by_partial_link_text("").click()

# 进入热搜页面
search_text = driver.find_element_by_xpath('//*[@id="s-hotsearch-content-wrapper"]/li[4]/a/span[2]').click()
driver.set_window_size(480, 800)  # 设置浏览器大小，参数数字为像素点
driver.maximize_window()  # 浏览器全屏

# 进入新闻页面
driver.get('http://news.baidu.com')
time.sleep(n)
# 返回到上一页面
driver.back()
# 刷新当前页面
driver.refresh()
# 前进到新闻页面
driver.forward()

search_text = driver.find_element_by_id('ww')
size = search_text.size
print("元素尺寸是：", size)
text = driver.find_element_by_xpath('//*[@id="footerwrapper"]/div[2]').text
print("元素文本是：", text)
attribute = search_text.get_attribute('type')
print("元素属性是：", attribute)
result = search_text.is_displayed()
print("设置元素是否可见：", result)
search_text.send_keys('测试')  # 模拟按键输入
search_text.clear()  # 清除文本
search_text.send_keys('再次输入测试')
driver.find_element_by_id('s_btn_wr').click()
# search_text.submit()

driver.quit()
