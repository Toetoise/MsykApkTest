from appium import webdriver
# from test_loginclass import Login
# from time import ctime
import re
# import subprocess
import time
import unittest
import os
import random

# 测试的包的路径和包名
appLocation = r"D:\appium_test_apk\Squirrel-V5.9.1.0-20200918-120961.apk"
# 读取设备 id
readDeviceId = list(os.popen('adb devices').readlines())
# 正则表达式匹配出 id 信息
deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
# 读取设备系统版本号
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]


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
        # if self.driver.is_app_installed("com.zdsoft.newsquirrel"):
        #     print("已安装美师优课，现执行卸载再安装新包")
        #     self.driver.remove_app("com.zdsoft.newsquirrel")
        #     self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        # Login(self.driver).login("guanyu47", "12345678")

    def is_element_exist(self, element):
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False

    def test_stuHomework(self):
        self.driver.find_element_by_id("com.zdsoft.newsquirrel:id/nav_btn_2").click()
        self.driver.find_element_by_xpath(
            "//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()
        question_num = len(self.driver.find_elements_by_xpath(
            "//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout"))
        i = 1
        while i < question_num + 1:
            if self.is_element_exist("单选题"):
                print("单选题")
                option_num = len(self.driver.find_elements_by_xpath("//android.widget.ListView/android.view.View"))
                option = random.randint(1, option_num)
                self.driver.find_element_by_xpath(
                    "//android.widget.ListView/android.view.View[{}]".format(option)).click()
                i = i + 1
            elif self.is_element_exist("阅读理解"):
                print("阅读理解")
                reading_num = len(self.driver.find_elements_by_xpath("//android.widget.ListView"))
                j = 1
                while j < reading_num + 1:
                    choice_num = len(self.driver.find_elements_by_xpath(
                        "//android.widget.ListView[{}]/android.view.View".format(j)))
                    choice = random.randint(1, choice_num)
                    self.driver.find_element_by_xpath(
                        "//android.widget.ListView[{0}]/android.view.View[{1}]".format(j, choice)).click()
                    time.sleep(3)
                    self.driver.swipe(1000, 850, 1000, 306, 1000)
                    j = j + 1
                i = i + 1
            elif self.is_element_exist("解答题"):
                print("解答题")
                self.driver.find_element_by_xpath("//*[@text='图片/视频']").click()
                self.driver.find_elements_by_id("com.zdsoft.newsquirrel:id/imageview_photo")[0].click()
                self.driver.find_elements_by_class_name('android.widget.Button')[1].click()
                self.driver.find_element_by_xpath("//*[@text='图片/视频']").click()
                self.driver.find_elements_by_id("com.zdsoft.newsquirrel:id/imageview_video")[0].click()
                self.driver.find_elements_by_class_name('android.widget.Button')[0].click()
                self.driver.swipe(1000, 900, 1000, 306, 1000)
                self.driver.swipe(1000, 900, 1000, 306, 1000)
                for k in range(4):
                    if self.is_element_exist("上传中..."):
                        time.sleep(10)
                self.driver.find_element_by_xpath("//*[@text='录音']").click()
                self.driver.find_element_by_id("com.zdsoft.newsquirrel:id/start_icon").click()
                time.sleep(5)
                self.driver.find_element_by_id("com.zdsoft.newsquirrel:id/start_icon").click()
                self.driver.find_element_by_xpath("//*[@text='上传录音']").click()

                i = i + 1
            else:
                print("不知道什么题型")
            self.driver.find_element_by_xpath(
                "//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[{}]".format(i)).click()
        print("完成")
        # questiontypes = ["//*[@text='单选题']", "//*[@text='阅读理解']", "//*[@text='解答题']", ]

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
