from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_username = (By.ID, "identifier-field")
        self.login_password = (By.NAME, "password")
        self.login_continue = (By.CSS_SELECTOR, "button.cl-button")

    def launch(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        (WebDriverWait(self.driver, 10)
            .until(EC.element_to_be_clickable(self.login_username))
            .send_keys(username, Keys.ENTER))

    def enter_password(self, password):
        (WebDriverWait(self.driver, 10)
            .until(EC.element_to_be_clickable(self.login_password))
            .send_keys(password, Keys.ENTER))

    def click_continue(self):
        self.driver.find_element(*self.login_continue).click()

    def login_title(self):
        assert self.driver.title == "Car Rental Service"