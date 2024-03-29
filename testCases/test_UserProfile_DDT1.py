import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.UserProfilePage1 import UserProfile_Class
from utilities import ExcelFileOperation
from utilities.readproperties1 import Readconfig


class Test_User_Profile_DDT:
    LoginUrl = Readconfig.getLoginUrl()
    RegistrationUrl = Readconfig.getRegistrationUrl()
    Username = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    path = "E:\\Automation\\Practice_Pytest_Credkart\\testCases\\TestData\\LoginData.xlsx"

    def test_UserLogin_ddt_006(self):
        # self.driver = setup
        self.driver = webdriver.Chrome()
        self.ur = UserProfile_Class(self.driver)
        self.rows = ExcelFileOperation.rows_count(self.path,'Sheet1')
        print(self.rows)
        List = []
        for r in range(2, self.rows + 1):
            self.email = ExcelFileOperation.ReadData(self.path, 'Sheet1', r, 1)
            self.password = ExcelFileOperation.ReadData(self.path, 'Sheet1', r, 2)
            self.Exp_Result = ExcelFileOperation.ReadData(self.path, 'Sheet1', r, 3)
            self.driver.get(self.LoginUrl)
            self.ur.Enter_Email(self.email)
            print("Username-->" + self.email)
            self.ur.Enter_Password(self.password)
            print("Password-->" + self.password)
            self.ur.Click_Login_Or_Registration()
            if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
                if self.Exp_Result == "Pass":
                    List.append("Pass")
                    self.driver.save_screenshot(
                        "E:\\Automation\\Practice_Pytest_Credkart\\Screenshots\\Login_Pass.png")
                    self.driver.find_element(By.XPATH, "//a[@role='button']").click()
                    self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
                    # assert True

                elif self.Exp_Result == "Fail":
                    List.append("Fail")
                    self.driver.save_screenshot(
                        "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Login_Pass.png")
                    # assert False

            else:  # Login Fail
                List.append("Fail")
                if self.Exp_Result == "Pass":
                    self.driver.save_screenshot(
                        "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Login_Pass.png")

                    # assert False
                elif self.Exp_Result == "Fail":
                    List.append("Pass")
                    self.driver.save_screenshot(
                        "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Login_Pass.png")
                    # assert True

                self.driver.save_screenshot(
                    "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Login_Fail.png")

        print(List)


# pytest -v --html=HTMLReports/Edge_Report.html --browser chrome -n=5 --alluredir="C:\Users\HP\Desktop\Python revision Jan 24\Pytest_Credkart\AllureReports"
# allure serve "folder Path"


#

# config -- > url, login id pass
# Logs
# Data Driven Test Case































































































