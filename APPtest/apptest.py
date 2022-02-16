from appium import webdriver
import unittest
import time

# 启动参数
desired_caps={
    'platformName':'Android',
    'platformVersion':'4.4.2',
    'deviceName':'127.0.0.1:62001',
    'appPackage':'com.android.settings',
    'appActivity':'.Settings'
}

class Settest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_seting(self):
        #查看WLAN
        self.driver.find_element_by_id("android:id/title").click()
        time.sleep(3)
        #回退到设置页面
        self.driver.find_element_by_id("android:id/up").click()
        time.sleep(3)
        #打开显示页面（当各菜单元素相同时用模拟手指点击（tap），取bounds的值,后面的500是持续时间，单位毫秒）
        element_info=self.driver.tap([(87,505),(141,542)],500)
        time.sleep(3)
        #返回到设置页面
        self.driver.find_element_by_id("android:id/up").click()
        time.sleep(3)

    def tearDown(self):
        #关闭驱动
        self.driver.quit()