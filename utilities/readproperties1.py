import configparser

config = configparser.RawConfigParser()
config.read("E:\\Automation\\Practice_Pytest_Credkart\\Configuration\\config.ini")     # ini file ka path under configuration folder


class Readconfig():

    @staticmethod
    def getLoginUrl():
        LoginUrl = config.get('user info', 'LoginUrl')
        return LoginUrl

    @staticmethod
    def getRegistrationUrl():
        RegistrationUrl = config.get('user info', 'RegistrationUrl')
        return RegistrationUrl

    @staticmethod
    def getUsername():
        Username= config.get('user info', 'User_email')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('user info', 'Password')
        return Password


































































































