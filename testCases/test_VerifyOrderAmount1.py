from selenium.webdriver.common.by import By

from selenium import webdriver
from pageObjects.UserProfilePage1 import UserProfile_Class
from pageObjects.VerifyOrderAmount_Page1 import VerifyOrderAmount_Class


class Test_VerifyAmount:

    def test_VerifyAmount(self, setup):
        self.driver = setup
        self.driver = webdriver.Firefox()
        self.ur = UserProfile_Class(self.driver)
        self.voa = VerifyOrderAmount_Class(self.driver)

        self.driver.get("https://automation.credence.in/login")

        self.ur.Enter_Email("puja12@gmail.com")
        self.ur.Enter_Password("Puja@123")
        self.ur.Click_Login_Or_Registration()
        self.voa.Click_AppleMacBook()
        self.voa.Click_AddToCart()
        self.voa.Click_ContinueShoppingButton()
        self.voa.Click_AppleIPad()
        self.voa.Click_AddToCart()
        self.voa.Click_ContinueShoppingButton()
        self.voa.Click_HeadPhone()
        self.voa.Click_AddToCart()
        if self.voa.Validate_Amount() == "Amount is Matched":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
