import pytest
from selenium import webdriver

# Use inbuilt hookup addoption from python
def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()

    elif browser == 'firefox':
        driver = webdriver.Firefox()

    elif browser == 'edge':
        driver = webdriver.Edge()

    else:
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    return driver

@pytest.fixture(params=[
    ('Admin','admin123','Pass'),
    ('Admin1', 'admin123', 'Fail'),
    ('Admin', 'admin1231', 'Fail'),
    ('Admin1', 'admin1231', 'Fail')
])
def getDataForLogin(request):
    return request.param
