from appium import webdriver
import time

# 启动参数
desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
#time.sleep(3)
# 生成一个driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
#查看WLAN
driver.find_element_by_id("android:id/title").click()
time.sleep(3)
#回退到设置页面
driver.find_element_by_id("android:id/up").click()
time.sleep(3)
#打开显示页面（当各菜单元素相同时用模拟手指点击（tap），取bounds的值,后面的500是持续时间，单位毫秒）
driver.tap([(87,505),(141,542)],500)
time.sleep(3)
#返回到设置页面
driver.find_element_by_id("android:id/up").click()
time.sleep(3)
#关闭驱动
driver.quit()