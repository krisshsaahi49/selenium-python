import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.relative_locator import locate_with

class TestCarrental:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.delete_all_cookies()
        yield driver
        driver.close()
        driver.quit()

    @pytest.mark.parametrize("username, password", [("test","test"),("test_user1","test"),("aditya","aditya")])
    def test_login(self, driver, username, password):
        driver.get("https://automation.krisshsaahi.dev")
        driver.refresh()
        time.sleep(3)
        driver.find_element(By.ID, value="identifier-field").send_keys(username, Keys.ENTER)
        time.sleep(3)
        driver.find_element(By.NAME, value="password").send_keys(password, Keys.ENTER)
        print(driver.title + ' ' + driver.current_url)
        time.sleep(3)

    def test_carrental_home(self, driver):

        # Navigate
        driver.get("https://automation.krisshsaahi.dev")
        driver.refresh()
        time.sleep(3)
        driver.find_element(By.ID, value="identifier-field").send_keys("test", Keys.ENTER)
        time.sleep(3)
        driver.find_element(By.NAME, value="password").send_keys("test", Keys.ENTER)
        print(driver.title + ' ' + driver.current_url)
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, value="Explore Cars").click()
        price = Select(driver.find_element(By.XPATH, value="(//select)[1]"))
        price.select_by_index(2)
        manufacturer = Select(driver.find_element(By.XPATH, value="(//select)[2]"))
        manufacturer.select_by_index(2)
        time.sleep(3)
        manufacturer.select_by_value("Toyota")
        time.sleep(3)
        price.select_by_visible_text("Low to High")
        time.sleep(3)

    def test_carrental_booking(self, driver):

        # Navigate
        driver.get("https://automation.krisshsaahi.dev")
        driver.refresh()
        time.sleep(3)
        driver.find_element(By.ID, value="identifier-field").send_keys("test", Keys.ENTER)
        time.sleep(3)
        driver.find_element(By.NAME, value="password").send_keys("test", Keys.ENTER)
        print(driver.title + ' ' + driver.current_url)
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, value="Explore Cars").click()
        price = Select(driver.find_element(By.XPATH, value="(//select)[1]"))
        price.select_by_index(2)
        manufacturer = Select(driver.find_element(By.XPATH, value="(//select)[2]"))
        manufacturer.select_by_index(2)
        time.sleep(3)
        manufacturer.select_by_value("Toyota")
        time.sleep(3)
        price.select_by_visible_text("Low to High")
        time.sleep(3)

        wait = WebDriverWait(driver, 10)
        four_runner = driver.find_element(By.XPATH, value="//h2[contains(text(),'4Runner')]")
        # rent_now = driver.find_element(locate_with(By.XPATH, "//h2[contains(text(),'4Runner')]").below({By.LINK_TEXT, 'Rent Now'}))
        rent_now = driver.find_element(By.XPATH,
                                       value="//h2[contains(text(),'4Runner')]//parent::div//button[text()='Rent Now']")

        action = ActionChains(driver)

        action.scroll_to_element(four_runner).move_to_element(four_runner).pause(3).move_to_element(
            rent_now).click().perform()
        time.sleep(3)

        location = Select(driver.find_element(By.NAME, "location"))
        location.select_by_visible_text("Indianapolis")

        pickup_date = driver.find_element(By.NAME, "pickUpDate")
        dropoff_date = driver.find_element(By.NAME, "dropOffDate")
        pickup_time = driver.find_element(By.NAME, "pickUpTime")
        dropoff_time = driver.find_element(By.NAME, "dropOffTime")

        (
            action.send_keys_to_element(pickup_date, "2024")
            .send_keys(Keys.ARROW_LEFT).send_keys(Keys.ARROW_LEFT)
            .send_keys("12").pause(2).send_keys("12")
            .send_keys_to_element(dropoff_date, "2024")
            .send_keys(Keys.ARROW_LEFT).send_keys(Keys.ARROW_LEFT)
            .send_keys("12").pause(2).send_keys("13")
            .send_keys_to_element(pickup_time, "11:54AM").pause(2)
            .send_keys_to_element(dropoff_time, "11:55AM").pause(2)
            .move_to_element(driver.find_element(By.NAME, value="contactNumber"))
            .click()
            .send_keys("8887672991")
            .perform())

        time.sleep(3)
        driver.save_screenshot('./image.png')
        driver.find_element(By.XPATH, value="//button[text()='Save']").click()

        time.sleep(3)