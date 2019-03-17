__author__ = 'Ratnesh Mallah'

from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetup","setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com","abcabc")
        result = self.lp.verifuLoginSuccessfully()
        assert result == True

    @pytest.mark.run(order=1)
    def test_InvalidLogin(self):
        self.lp.login("testfail@email.com","abcabc")
        result = self.lp.verifyInvalidLogin()
        assert result == True

