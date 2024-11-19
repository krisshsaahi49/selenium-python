from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.homepage_explorecars = (By.LINK_TEXT, "Explore Cars")
        self.homepage_sortprice = (By.XPATH, "(//select)[1]")
        self.homepage_manufacturer = (By.XPATH, "(//select)[2]")
        self.homepage_4runner = (By.XPATH, "//h2[contains(text(),'4Runner')]")
        self.homepage_rent4runner = (By.XPATH,"//h2[contains(text(),'4Runner')]//parent::div//button[text()='Rent Now']")
        self.homepage_location = (By.NAME, "location")
        self.homepage_pickup_date = (By.NAME, "pickUpDate")
        self.homepage_dropoff_date = (By.NAME, "dropOffDate")
        self.homepage_pickup_time = (By.NAME, "pickUpTime")
        self.homepage_dropoff_time = (By.NAME, "dropOffTime")
        self.homepage_contact_number = (By.NAME, "contactNumber")
        self.homepage_save = (By.XPATH, "//button[text()='Save']")

    def goto_4runner(self):
        (((ActionChains(self.driver).scroll_to_element(self.driver.find_element(*self.homepage_4runner))
            .move_to_element(self.driver.find_element(*self.homepage_4runner))).pause(2)
            .move_to_element(self.driver.find_element(*self.homepage_rent4runner)))
            .click()
            .perform())

    def rent_car(self, location):
        # Select location from the dropdown
        select_location = Select(self.driver.find_element(*self.homepage_location))
        select_location.select_by_visible_text(location)

        # Input pickup and dropoff dates
        pickup_date_field = self.driver.find_element(*self.homepage_pickup_date)
        dropoff_date_field = self.driver.find_element(*self.homepage_dropoff_date)
        pickup_time_field = self.driver.find_element(*self.homepage_pickup_time)
        dropoff_time_field = self.driver.find_element(*self.homepage_dropoff_time)
        contact_number_field = self.driver.find_element(*self.homepage_contact_number)

        action = ActionChains(self.driver)

        # Enter pickup date
        action.send_keys_to_element(pickup_date_field, "2024").send_keys(Keys.ARROW_LEFT).send_keys(Keys.ARROW_LEFT)
        action.send_keys("12").pause(1).send_keys("12").perform()

        # Enter dropoff date
        action.send_keys_to_element(dropoff_date_field, "2024").send_keys(Keys.ARROW_LEFT).send_keys(Keys.ARROW_LEFT)
        action.send_keys("12").pause(1).send_keys("13").perform()

        # Enter pickup and dropoff times
        action.send_keys_to_element(pickup_time_field, "11:54AM").pause(1).perform()
        action.send_keys_to_element(dropoff_time_field, "11:55AM").pause(1).perform()

        # Enter contact number
        action.click(contact_number_field).send_keys("8887672991").perform()

        # Click on Save
        self.driver.find_element(*self.homepage_save).click()