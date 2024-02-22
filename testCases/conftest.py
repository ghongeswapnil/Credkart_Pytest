import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options


# In pytest, hook functions are functions that can be used to extend or
# modify the behavior of pytest. They are called automatically by pytest at
# specific times during the test run.

# The pytest_configure function is a hook function in pytest that is called once the
# configuration object has been created and all plugins and initial conftest files has been loaded.

# The pytest_addoption function is a hook function in pytest that is used to add custom command-line options to the
# pytest command. It takes a single argument, parser, which is an instance of the argparse. ArgumentParser class.


# add arg --browser this is for your command liner

def pytest_addoption(parser):
    parser.addoption("--browser")


# passing the value to --browser

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Define the browser fixture function with a single argument, request.
# Within the browser function, use the request.config.getoption() method to get the value
# of the --browser option passed to pytest on the command line.


# here we are passing actual value to --browser

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print("Launching Chrome Browser")
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        print("Launching Firefox Browser")
        driver = webdriver.Firefox()
    elif browser == 'edge':
        print("Launching Edge Browser")
        driver = webdriver.Edge()
    # if browser == 'headless':
    else:
        print("Headless mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


# def pytest_metadata(metadata):                         # By using this we can make changes in Html reports
#     metadata["Project Name"] = "CredKart"
#     metadata["Environment"] = "QA Environment"
#     metadata["Module"] = "User Profile"
#     metadata["Tester"] = "Swapnil"
#     metadata.pop("Plugins", None)
#
@pytest.fixture(params=[

    ("puja12@gmail.com","Puja@123","Pass"),
    ("puja12@gmail.com","Puja@1234","Fail"),
    ("puja121@gmail.com","Puja@123","Fail"),
    ("puja121@gmail.com","Puja@1234","Fail")

])

def getDataForLogin(request):
    return request.param





































# @pytest.fixture()
# def setup():
#     driver = webdriver.Firefox()
#     return driver
