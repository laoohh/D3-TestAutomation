import time
import pytest
import softest
from pages.search_flights_results_page import SearchFlightsResultsPage
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter(softest.TestCase):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #self.driver.implicitly_wait(10)
        self.driver.get("https://yatra.com")
        self.driver.maximize_window()

        self.lanchpage = LaunchPage(self.driver)
        self.ut = Utils()

    def __del__(self):
        self.driver.close()

    # @pytest.fixture(autouse=True)
    # def class_setup(self):
    #     self.lanchpage = LaunchPage(self.driver)
    #     self.ut = Utils()

    def test_search_flights_1_stop(self):
        # Lanching browser and opening the travel website
        # Provide going fro location

        search_flight_results_page = self.lanchpage.searchFlights("New Delhi", "New York", "24/08/2021")

        # #lp.departfrom("New Delhi")
        # lp.enterDeparFromLocation("New Delhi")
        #
        # # Provide going to location
        # lp.enterGoingToLocation("New York")
        # time.sleep(3)
        #
        # # to resolve sync issues
        # # Select the departure date
        # lp.enterDepartureDate("24/08/2021")
        # time.sleep(3)
        #
        # # Click on flight search button
        # lp.clickSearchFlightsButton()
        # time.sleep(3)

        # to handle dynamic scroll
        self.lanchpage.page_scroll()

        # Select the filter 1 stop
        #sf = SearchFlightsResultsPage(self.driver)
        search_flight_results_page.filter_flights_by_stop("1 Stop")
        time.sleep(3)

        # Verify that filtered results show flights having only 1 stop
        allstops1 = search_flight_results_page.get_search_flight_results()
        #allstops1 = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
        #        "//span[contains(text(), 'Non Stop') or contains(text(), '1 Stop') or contains(text(), '2 Stop')]")))
        print(len(allstops1))

        time.sleep(4)


        self.ut.assertListItemText(allstops1, "1 Stop")



    # def test_search_flights_2_stop(self):
    #     search_flight_results_page = self.lanchpage.searchFlights("New Delhi", "JFK", "24/08/2021")
    #     self.lanchpage.page_scroll()
    #
    #     # Select the filter 1 stop
    #     search_flight_results_page.filter_flights_by_stop("2 Stop")
    #     time.sleep(3)
    #
    #     # Verify that filtered results show flights having only 1 stop
    #     allstops1 = search_flight_results_page.get_search_flight_results()
    #     print(len(allstops1))
    #     time.sleep(4)
    #
    #     self.ut.assertListItemText(allstops1, "2 Stop")


test = TestSearchAndVerifyFilter()
test.test_search_flights_1_stop()
#test.test_search_flights_2_stop()
