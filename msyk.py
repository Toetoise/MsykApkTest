from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
# from test_loginclass import Login
# from time import ctime
import re
# import subprocess
import time
import unittest
import os
import random
import threading

# 测试的包的路径和包名
appLocation = r"D:\appium_test_apk\Squirrel-V5.9.6-20201110-121858.apk"
# 读取设备 id
readDeviceId = list(os.popen('adb devices').readlines())
# 正则表达式匹配出 id 信息
deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
# 读取设备系统版本号
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]

cond = threading.Condition()
# cond.acquire()
# cond.release()
# cond.wait()
# cond.notify()

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

    def test_teaPercenter(self):
        self.driver.find_element_by_class_name("com.zdsoft.newsquirrel:id/teacher_main_user_line").click()
        self.driver.find_element_by_xpath("//*[@text='修改密码']").click()
        self.driver.find_element_by_xpath("//*[@text='旧密码']").send_keys("Msyk_741")
        self.driver.find_element_by_xpath("//*[contains(@text, '新密码')]").send_keys("12345678")
        self.driver.find_element_by_xpath("//*[@text='确认密码']").send_keys("12345678")
        self.driver.find_element_by_xpath("//*[@text='确认修改']").click()
        self.driver.find_element_by_xpath("//*[@text='清空缓存']").click()
        if self.is_element_exist("0.00KB"):
            print("缓存清理成功")
        else:
            print("缓存清理失败，再清理一次")
            self.driver.find_element_by_xpath("//*[@text='清空缓存']").click()
            if self.is_element_exist("0.00KB"):
                print("缓存清理成功")
        self.driver.find_element_by_xpath("//*[@text='清理文件']").click()
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        self.driver.find_element_by_xpath("//*[@text='关于美师优课']").click()
        self.driver.find_element_by_xpath("//*[contains(@text, '用户服务协议')]").click()
        self.driver.find_element_by_xpath("//*[@text='我知道了']").click()

    def test_teaHomework(self):
        self.driver.find_element_by_xpath("//*[@text='作业']").click()
        self.driver.find_element_by_id("com.zdsoft.newsquirrel:id/add_homework_layout").click()
        self.driver.find_element_by_id("com.zdsoft.newsquirrel:id/name_edit").send_keys("自动化作业")
        self.driver.find_element_by_id("com.zdsoft.newsquirrel:id/tv_homeWork_end_time").click()
        year = self.driver.find_element_by_id("com.zdsoft.newsquirrel:id/picker_year")
        hour = self.driver.find_element_by_id("com.zdsoft.newsquirrel:id/picker_hour")
        minute = self.driver.find_element_by_id("com.zdsoft.newsquirrel:id/picker_minute")
        sure = self.driver.find_element_by_id("com.zdsoft.newsquirrel:id/tv_pick_sure")
        action1 = TouchAction(self.driver)
        action2 = TouchAction(self.driver)
        action3 = TouchAction(self.driver)
        action4 = MultiAction(self.driver)
        action1.press(year).move_to(sure).release()
        action2.press(hour).move_to(sure).release()
        action3.press(minute).move_to(sure).release()
        action4.add(action1, action2, action3)
        action4.perform()
        self.driver.find_element_by_xpath("//*[@text='创建并下一步']").click()
        self.driver.find_element_by_id("com.zdsoft.newsquirrel:id/teacher_homework_my_material").click()

    def test_teaMaterial(self):
        self.driver.find_element_by_xpath("//*[@text='素材库']").click()
        # 上传素材
        self.driver.find_element_by_xpath("//*[@text='素材上传']").click()
        self.driver.find_element_by_xpath("//*[@text='题库上传']").click()
        self.driver.find_element_by_xpath("//*[@text='PPT上传']").click()
        self.driver.find_element_by_xpath("//*[@text='新建文件夹']").click()

    def test_teaCourseware(self):
        self.driver.find_element_by_xpath("//*[@text='备课']").click()
        self.driver.find_element_by_xpath("//*[@text='新建教学设计']").click()

    def test_teaClassrecord(self):
        self.driver.find_element_by_xpath("//*[@text='课堂']").click()
        self.driver.find_element_by_class_name("com.zdsoft.newsquirrel:id/iv_more").click()
        self.driver.find_element_by_xpath("//*[@text='历史课堂']").click()

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
                self.driver.find_element_by_class_name("android.widget.Button").click()

                i = i + 1
            else:
                print("不知道什么题型")
            self.driver.find_element_by_xpath(
                "//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[{}]".format(i)).click()
        print("完成")
        # questiontypes = ["//*[@text='单选题']", "//*[@text='阅读理解']", "//*[@text='解答题']", ]

    def test_stuPercenter(self):
        self.driver.find_element_by_xpath("//*[@text='进入个人中心']").click()
        self.driver.find_element_by_xpath("//*[@text='个人信息']").click()
        self.driver.find_element_by_class_name('com.zdsoft.newsquirrel:id/back_title').click()
        self.driver.find_element_by_class_name('com.zdsoft.newsquirrel:id/iv_eye_control').click()
        self.driver.find_element_by_class_name('com.zdsoft.newsquirrel:id/iv_eye_control').click()
        self.driver.find_element_by_xpath("//*[@text='修改密码']").click()
        self.driver.find_element_by_xpath("//*[@text='旧密码']").send_keys("12345678")
        self.driver.find_element_by_xpath("//*[contains(@text, '新密码，')]").send_keys("123456789")
        self.driver.find_element_by_xpath("//*[@text='确认新密码']").send_keys("123456789")
        self.driver.find_element_by_class_name('com.zdsoft.newsquirrel:id/st_change_confirm').click()
        self.driver.find_element_by_xpath("//*[@text='清空缓存']").click()
        if self.is_element_exist("0.00KB"):
            print("缓存清理成功")
        else:
            print("缓存清理失败，再清理一次")
            self.driver.find_element_by_xpath("//*[@text='清空缓存']").click()
            if self.is_element_exist("0.00KB"):
                print("缓存清理成功")
        self.driver.find_element_by_xpath("//*[@text='关于平台']").click()
        self.driver.find_element_by_xpath("//*[contains(@text, '用户服务协议')]").click()
        self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
        self.driver.find_element_by_class_name('com.zdsoft.newsquirrel:id/close_btn').click()
        # self.driver.find_element_by_class_name('com.zdsoft.newsquirrel:id/student_exit_bt').click()   # 退出登录
        self.driver.find_element_by_class_name('com.zdsoft.newsquirrel:id/back_title').click()

    def test_stuClassrecord(self):
        self.driver.find_element_by_class_name('com.zdsoft.newsquirrel:id/nav_btn_5').click()
        self.driver.find_element_by_xpath("//*[contains(@text, '历史课堂')]").click()

    def test_stuClassroom(self):
        self.driver.find_element_by_class_name('com.zdsoft.newsquirrel:id/nav_btn_5').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
