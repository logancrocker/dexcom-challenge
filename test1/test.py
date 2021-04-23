import unittest
import page
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestUserLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://clarity.dexcom.com/")

    def test_user_login(self):
        landingPage = page.LandingPage(self.driver)
        assert landingPage.title_matches()
        landingPage.clickUserButton()
        loginPage = page.LoginPage(self.driver)
        assert loginPage.title_matches()
        loginPage.login()
        welcomePage = page.WelcomePage(self.driver)
        self.driver.implicitly_wait(5)
        assert welcomePage.logged_in()

    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main()