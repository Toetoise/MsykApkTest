from appium import webdriver
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
    # def appiumserver_start(host, port):
    #     """启动appium server"""
    #     cmd = 'start /b appium -a ' + str(host) + ' -p ' + str(port) + ' -bp ' + str(str(port + 1))
    #     print('%s at %s' % (cmd, ctime()))
    #     subprocess.Popen(cmd, shell=True, stdout=open('../test_case/' + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)
    #
    # if __name__ == '__main__':
    #     host = '127.0.0.1'
    #     port = 4723
    #     appiumserver_start(host, port)

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
            ''
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(msykAppTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
