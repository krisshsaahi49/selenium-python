import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.loginpage import LoginPage

URL = "https://automation.krisshsaahi.dev"

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=options)
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.close()
    driver.quit()

@pytest.mark.parametrize("username, password", [("test","test"),("test_user1","test"),("aditya","aditya")])
def test_signin(driver, username, password):
    login = LoginPage(driver)
    login.launch(URL)
    login.enter_username(username)
    login.enter_password(password)
    login.login_title()

def test_rentacar(driver):
    test_signin(driver,"test","test")
    from pages.homepage import HomePage
    home = HomePage(driver)
    home.goto_4runner()
    home.rent_car("Indianapolis")
