class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class LandingPage(BasePage):
    def title_matches(self):
        return "Dexcom CLARITY" in self.driver.title

    def clickUserButton(self):
        user_button = self.driver.find_element_by_xpath("//*[contains(text(), 'Dexcom CLARITY for Home Users')]")
        user_button.click()

class LoginPage(BasePage):
    def title_matches(self):
        return "Dexcom - Account Management" in self.driver.title

    def login(self):
        username_field = self.driver.find_element_by_id("username")
        password_field = self.driver.find_element_by_id("password")
        username_field.send_keys("codechallenge")
        password_field.send_keys("Password123")
        login_button = self.driver.find_element_by_name("op")
        login_button.click()

class WelcomePage(BasePage):
    def logged_in(self):
        return self.driver.find_element_by_class_name("home-user-header__logout.cui-link")
