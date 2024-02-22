import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.UserProfilePage1 import UserProfile_Class

def generate_random_email():
    name = "puja"
    numbers = ''.join(random.choices(string.digits, k=3))  # You can adjust the number of digits as needed
    email = f"{name}{numbers}@gmail.com"
    return email






class Test_User_Profile:

    def test_UserRegistration_001(self,setup):
        self.driver = setup
        # 1 Browser Open
        # self.driver = webdriver.Firefox()
        self.ur = UserProfile_Class(self.driver)

        # 2 Go to registration url
        self.driver.get("https://automation.credence.in/register")

        # 3 Enter Name
        # self.driver.find_element(By.ID, "name").send_keys("Puja")
        self.ur.Enter_Name("Puja")

        # 4 Enter EMail ID
        # self.driver.find_element(By.ID, "email").send_keys("puja12@gmail.com")
        email=generate_random_email()
        self.ur.Enter_Email(email)

        # 5 Enter Password
        # self.driver.find_element(By.ID, "password").send_keys("Puja@123")
        self.ur.Enter_Password("Puja@123")

        # 6 Enter Confirm Password
        # self.driver.find_element(By.ID, "password-confirm").send_keys("Puja@123")
        self.ur.Enter_Confirm_Password("Puja@123")

        # 7 Click on Register Button
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.ur.Click_Login_Or_Registration()

        # 8 Validate Registration
        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Registration Pass")
            assert True
        except:
            print("Registration Fail")
            assert False

        if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
            self.driver.save_screenshot(
                "E:\Automation\Practice_Pytest_Credkart\Screenshots\Registration_Pass.png")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(
                "E:\Automation\Practice_Pytest_Credkart\Screenshots\Registration_Fail.png")
            self.driver.close()
            assert False

    def test_UserLogin_002(self, setup):
        self.driver = setup
        # 1 Browser Open
        # self.driver = webdriver.Firefox()
        self.ur = UserProfile_Class(self.driver)
        # 2 Go to Url https://automation.credence.in/login
        self.driver.get("https://automation.credence.in/login")
        # 3 Enter email
        # self.driver.find_element(By,XPATH, "//input[@id='email']").send_keys("puja12@gmail.com")
        self.ur.Enter_Email("puja12@gmail.com")
        # 4 Enter Password
        # self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Puja@123")
        self.ur.Enter_Password("Puja@123")
        # 5 Click on Login Button
        # self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.ur.Click_Login_Or_Registration()
        # 6 Validate Login
        if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
            self.driver.save_screenshot("E:\Automation\Practice_Pytest_Credkart\Screenshots\Login_Pass.png")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("E:\Automation\Practice_Pytest_Credkart\Screenshots\Login_Fail.png")

# pytest -v --html=HTMLReports/Edge_Report.html --browser edge -n=3 --alluredir="C:\Users\HP\Desktop\Python revision Jan 24\Pytest_Credkart\AllureReports"
# allure serve "folder Path"


#

# config -- > url, login id pass
# Logs
# Data Driven Test Case
