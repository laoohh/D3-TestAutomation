import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def setup(request, browser, url):
    # Lanching browser and opening the travel website
    if (browser=="chrome"):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif (browser=="firefox"):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif (browser=="edge"):
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    #driver.implicitly_wait(10)
    driver.get("https://yatra.com")  #url
    driver.maximize_window()
    request.cls.driver = driver

    yield

    driver.close()


@pytest.fixture()
def TestCaseSetup():
    print("click menu")
    yield
    print("end of test case")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session", autouse=True)
def url(request):
    return request.config.getoption("--url")
