from appium import webdriver
from test_loginclass import Login
# from time import ctime
import re
# import subprocess
# import time
import unittest
import os

# 测试的包的路径和包名
appLocation = r"D:\appium_test_apk\Squirrel-V5.8.12.2-20200817-120122.apk"
# 读取设备 id
readDeviceId = list(os.popen('adb devices').readlines())
# 正则表达式匹配出 id 信息
deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
# 读取设备系统版本号
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]


# 删除以前的安装包
# os.system('adb uninstall ' + "com.zdsoft.newsquirrel")

class msykAppTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'automationName': 'Appium',
            'platformName': 'Android',
            'platformVersion': deviceVersion,
            'deviceName': deviceId,
            'appPackage': 'com.zdsoft.newsquirrel',
            'appWaitPackage': 'com.zdsoft.newsquirrel',
            'app': appLocation,
            'appActivity': ".android.activity.StartActivity",
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        # Login(self.driver).login("nls_1", "Msyk_123")

    def test_stuHomework(self):
        self.driver.find_element_by_xpath("//*[@text='去完成作业']").click()
        self.driver.find_element_by_xpath("//*[@text='【预习】自动化测试1']").click()
        self.driver.find_element_by_xpath("//*[@text='A.']").click()
        print("123")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
