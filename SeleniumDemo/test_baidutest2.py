# Generated by Selenium IDE
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class TestBaidutest2:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_baidutest2(self):
        # Test name: baidu_test_2
        # Step # | name | target | value
        # 1 | runScript | window.scrollTo(0,0) |
        self.driver.execute_script("window.scrollTo(0,0)")
        # 2 | type | id=kw | test
        self.driver.find_element(By.ID, "kw").send_keys("test")
        # 3 | click | id=su |
        self.driver.find_element(By.ID, "su").click()
        # 4 | runScript | window.scrollTo(0,0) |
        self.driver.execute_script("window.scrollTo(0,0)")
        # 5 | click | css=p:nth-child(6) > .nav |
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(6) > .nav").click()
        # 6 | click | css=.navbar-toggle |
        self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggle").click()
        # 7 | click | linkText=码上行动 |
        self.vars["window_handles"] = self.driver.window_handles
        # 8 | storeWindowHandle | root |
        self.driver.find_element(By.LINK_TEXT, "码上行动").click()
        # 9 | selectWindow | handle=${win327} |
        self.vars["win327"] = self.wait_for_window(2000)
        # 10 | click | css=.navbar-toggle |
        self.vars["root"] = self.driver.current_window_handle
        # 11 | click | linkText=编程实例 |
        self.driver.switch_to.window(self.vars["win327"])
        # 12 | click | linkText=71. 打包为可执行文件 |
        self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggle").click()
        # 13 | click | linkText=登录 |
        self.driver.find_element(By.LINK_TEXT, "编程实例").click()
        # 14 | type | id=username | anne
        self.driver.find_element(By.LINK_TEXT, "71. 打包为可执行文件").click()
        # 15 | type | id=password | BMGW5425@yt
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        # 16 | click | css=.ui-btn > input |
        self.driver.find_element(By.ID, "username").send_keys("anne")
        # 17 | click | linkText=71. 打包为可执行文件 |
        self.driver.find_element(By.ID, "password").send_keys("BMGW5425@yt")
        # 18 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".ui-btn > input").click()
        # 19 | click | css=p:nth-child(5) > .nav |
        self.driver.find_element(By.LINK_TEXT, "71. 打包为可执行文件").click()
        # 20 | click | linkText=习题集 |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 21 | click | linkText=习题13：查询热映电影 |
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(5) > .nav").click()
        # 22 | mouseOver | css=#cls_btn > img |
        self.driver.find_element(By.LINK_TEXT, "习题集").click()
        # 23 | click | css=.headContent |
        self.driver.find_element(By.LINK_TEXT, "习题13：查询热映电影").click()
        # 24 | click | css=.headContent |
        element = self.driver.find_element(By.CSS_SELECTOR, "#cls_btn > img")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 25 | click | css=.headContent |
        self.driver.find_element(By.CSS_SELECTOR, ".headContent").click()
        # 26 | click | css=.hover |
        self.driver.find_element(By.CSS_SELECTOR, ".headContent").click()
        # 27 | click | id=compareTargetSel |
        self.driver.find_element(By.CSS_SELECTOR, ".headContent").click()
        # 28 | close |  |
        self.driver.find_element(By.CSS_SELECTOR, ".hover").click()
        # 29 | selectWindow | handle=${root} |
        self.driver.find_element(By.ID, "compareTargetSel").click()
        # 30 | close |  |
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.close()
