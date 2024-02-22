from selenium.webdriver.common.by import By


class Registration_Class:
    Text_Name_ID = (By.ID, "name")
    Text_Email_ID = (By.ID, "email")
    Text_Password_ID = (By.ID, "password")
    Text_ConfirmPassword_ID = (By.ID, "password-confirm")
    Click_Register_XPATH = (By.XPATH, "//button[@type='submit']")
    Validate_Registration_XPATH = (By.XPATH, "//h2[normalize-space()='CredKart']")

    def __init__(self, driver):
        self.driver = driver

    def Enter_Name(self, name):
        self.driver.find_element(*Registration_Class.Text_Name_ID).send_keys(name)

    def Enter_Email(self, email):
        self.driver.find_element(*Registration_Class.Text_Email_ID).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*Registration_Class.Text_Password_ID).send_keys(password)

    def Enter_Confirm_Password(self, confirm_password):
        self.driver.find_element(*Registration_Class.Text_ConfirmPassword_ID).send_keys(confirm_password)

    def Click_RegisterButton(self):
        self.driver.find_element(*Registration_Class.Click_Register_XPATH).click()

    def Validate_Registration(self):
        try:
            self.driver.find_element(*Registration_Class.Validate_Registration_XPATH)
            print("Registration Pass")
            return "Registration Pass"
        except:
            print("Registration Fail")
            return "Registration Fail"
















































































































