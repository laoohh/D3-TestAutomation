import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver
from pages.search_flights_results_page import SearchFlightsResultsPage


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #self.wait = wait

    # Locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD    = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD = "//label[@for='BE_flight_origin_date']"
    ALL_DATES         = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD' and @class!='inActiveTD weekend']"
    SEARCH_BUTTON     = "//input[@value='Search Flights']"

    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getGoingToResults(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

    def getDepartureDateFieldField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDatesField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES).find_elements(By.XPATH, self.ALL_DATES)

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    # Provide going fro location
    def enterDeparFromLocation(self, deparlocation):
        depart_from_field = self.getDepartFromField()
        depart_from_field.click()
        depart_from_field.send_keys(deparlocation)
        depart_from_field.send_keys(Keys.ENTER)

        search_flight_results_page = SearchFlightsResultsPage(self.driver)
        return search_flight_results_page

    # def departfrom(self, departlocation):
    #     # Provide going fro location
    #     depart_from = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_city']")
    #         #self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
    #     depart_from.click()
    #     depart_from.send_keys(departlocation)
    #     depart_from.send_keys(Keys.ENTER)

    # Provide going to location
    def enterGoingToLocation(self, goingtolocation):
        going_to_field = self.getGoingToField()
        going_to_field.click()
        time.sleep(2)
        going_to_field.send_keys(goingtolocation)

        search_results = self.getGoingToResults()
        for result in search_results:
            if "New York (JFK)" in result.text:
                result.click()
                break

    # def goingto(self, goingtolocation):
    #     # Provide going to location
    #     #going_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']" )))
    #     going_to = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_arrival_city']")
    #     going_to.click()
    #     time.sleep(2)
    #     going_to.send_keys(goingtolocation)
    #
    #     #search_results = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]/li")))
    #     search_results = self.wait_for_presence_of_all_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
    #
    #     for result in search_results:
    #         if "New York (JFK)" in result.text:
    #             result.click()
    #             break

    def enterDepartureDate(self, departuredate):
        self.getDepartureDateFieldField().click()
        all_dates = self.getAllDatesField()
        # Select the departure date
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break

    # def selectdate(self, departdate):
    #     # to resolve sync issues
    #     #self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
    #     self.wait_until_element_is_clickable(By.XPATH, "//label[@for='BE_flight_origin_date']").click()
    #
    #     #all_dates = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD' and @class!='inActiveTD weekend']"))) \
    #     #    .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD' and @class!='inActiveTD weekend']")
    #     all_dates = self.wait_until_element_is_clickable(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD' and @class!='inActiveTD weekend']").\
    #         find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD' and @class!='inActiveTD weekend']")
    #
    #
    #     # Select the departure date
    #     for date in all_dates:
    #         if date.get_attribute("data-date") == departdate:
    #             date.click()
    #             break

    def clickSearchFlightsButton(self):
        self.getSearchButton().click()
        time.sleep(4)

    # def clicksearchbutton(self):
    #     # Click on flight search button
    #     self.driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
    #     time.sleep(4)

    def searchFlights(self, departlocation, goingtolocation, departuredate):
        self.enterDeparFromLocation(departlocation)
        self.enterGoingToLocation(goingtolocation)
        self.enterDepartureDate(departuredate)
        self.clickSearchFlightsButton()

        search_flight_results_page = SearchFlightsResultsPage(self.driver)
        return search_flight_results_page

