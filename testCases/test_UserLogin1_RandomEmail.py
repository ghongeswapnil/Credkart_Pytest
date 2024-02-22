import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.RegistrationPage1 import Registration_Class


import random
import string
import pytest
from selenium import webdriver

# def generate_random_email():
#     username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
#     domain = ''.join(random.choices(string.ascii_lowercase, k=5))
#     extensions = ['com', 'net']             # yaha pe extension kuchch bhi de sakte hai ex. com,in,net,org   etc
#     extension = random.choice(extensions)
#     email = f"{username}@{domain}.{extension}"
#     return email

def generate_random_email():
    name = "puja"
    numbers = ''.join(random.choices(string.digits, k=3))  # You can adjust the number of digits as needed
    email = f"{name}{numbers}@gmail.com"
    return email

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Replace with the appropriate webdriver
    yield driver
    driver.quit()


class Test_User_Profile:

    def test_UserRegistration_001(self):
        # 1 Browser Open
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.ur = Registration_Class(self.driver)
        # 2 Go to registration url
        self.driver.get("https://automation.credence.in/register")

        # 3 Enter Name
        # self.driver.find_element(By.ID, "name").send_keys("Rohit")
        self.ur.Enter_Name("Puja")

        # 4 Enter EMail Id
        email=generate_random_email()
        # self.driver.find_element(By.ID,"email").send_keys("puja123@gmail.com")
        self.ur.Enter_Email(email)

        # 5 Enter Password
        # self.driver.find_element(By.ID, "password").send_keys("Puja@123")
        self.ur.Enter_Password("Puja@123")

        # 6 Enter Confirm Password
        # self.driver.find_element(By.ID, "password-confirm").send_keys("Puja@123")
        self.ur.Enter_Confirm_Password("Puja@123")

        # 7 Click on Register Button
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.ur.Click_RegisterButton()

        time.sleep(10)

        # 8 Validate Registration
        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Registration pass")
            assert True
        except:
            print("Registration Fail")
            assert False

        if self.ur.Validate_Registration() == "Registration Pass":
            assert True
        else:
            assert False
