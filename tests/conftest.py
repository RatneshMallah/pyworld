import pytest
import unittest
import platform
from selenium import webdriver
from base.web_driver_factory import WebDriverFactory


@pytest.yield_fixture()
def setUp():
    print("test going to be start")
    yield
    print("Test Done")


@pytest.yield_fixture(scope="class")
def oneTimeSetup(request,browser):
    baseUrl = "https://letskodeit.teachable.com/"
    wdf = WebDriverFactory(browser)

    if platform.system() != 'Linux':
        driver = wdf.getWindowsDriverInstance()
    else:
        driver = wdf.getLinuxDriverInstance()

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(baseUrl)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    print("Running oneTime TearDown")
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser",help="Browser name (EX : Chrome)")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
