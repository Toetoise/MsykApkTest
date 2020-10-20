class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element_by_xpath("//*[@text='请输入用户名']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@text='请输入密码']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@text='登 录']").click()