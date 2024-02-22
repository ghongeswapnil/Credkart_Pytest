import random
import string
import time

import self
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.UserProfilePage1 import UserProfile_Class
from utilities.readproperties1 import Readconfig
from utilities.Logger import Logging_Class


class Test_User_Profile:
    LoginUrl = Readconfig.getLoginUrl()
    RegistrationUrl = Readconfig.getRegistrationUrl()
    Username = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    log = Logging_Class.log_generator()

    def test_UserRegistration_001(self,setup):
        self.log.info("test_UserRegistration_001 is started")
        # self.log.debug("this is debug log")
        # self.log.info("this is info log")
        # self.log.warning("this is warning log")
        # self.log.error("this is error log")
        # self.log.critical("this is critical log")
        self.driver = setup
        self.log.info(" Opening Browser")
        # 1 Browser Open
        # self.driver = webdriver.Firefox()
        self.ur = UserProfile_Class(self.driver)
        # 2 Go to registartion url
        self.driver.get(self.RegistrationUrl)
        self.log.info("Going to Url-->" + self.RegistrationUrl)

        # 3 Enter Name
        # self.driver.find_element(By.ID, 'name').send_keys("Puja")
        self.ur.Enter_Name("Puja")
        self.log.info("Entering the name")

        # 4 Enter Email Id
        # self.driver.find_element(By.ID, 'email').send_keys("puja12345@gmail.com")
        email = Generate_Email()
        self.ur.Enter_Email(email)
        self.log.info("Entering the Email-->" + email)
        print(email)

        # 5 Enter Password
        # self.driver.find_element(By.ID, 'password').send_keys("Puja@123")
        self.ur.Enter_Password("Puja@123")
        self.log.info("Entering the password")

        # 6 Enter Confirm Password
        # self.driver.find_element(By.ID, "password-confirm").send_keys("Puja@123")
        self.ur.Enter_Confirm_Password("Puja@123")
        self.log.info("Entering the confirm password")

        # 7 Click on Register Button
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.ur.Click_Login_Or_Registration()
        self.log.info("Clicking on Register Button")

        # 8 Validate Registration
        # try:
        #     self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
        #     print("Registration Pass")
        #     assert True
        # except:
        #     print("Registration Fail")
        #     assert False

        if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
            self.log.info("test_UserRegistration_001 is pass")
            self.driver.save_screenshot(
                "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Registration_Pass.png")
            # self.driver.close()
            assert True
        else:
            self.log.info("test_UserRegistration_001 is fail")
            self.driver.save_screenshot(
                "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Registration_Fail.png")
            # self.driver.close()
            assert False
        self.log.info("test_UserRegistration_001 is completed")


def Generate_Email():
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])
    return f"{username}@{domain}"

















































































# pytest -v -s --browser chrome "E:\Automation\Practice_Pytest_Credkart\testCases\test_UserProfile_Logs.py" --html=HtmlReports/Log.html