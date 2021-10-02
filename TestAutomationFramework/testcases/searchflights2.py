import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixture("setup")
class TestSearchAndVerifyFilter():

    def test_search_flights(self):
        self.driver = request.cls.driver
        self.wait = request.cls.wait

        # Lanching browser and opening the travel website

        # Provide going fro location
        depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)
        time.sleep(2)

        # Provide going to location
        going_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']" )))
        going_to.click()
        time.sleep(2)
        going_to.send_keys("New York")

        search_results = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]/li")))

        for result in search_results:
            if "New York (JFK)" in result.text:
                result.click()
                break

        # to resolve sync issues
        # Select the departure date
        # to resolve sync issues
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        all_dates = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD' and @class!='inActiveTD weekend']"))) \
            .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD' and @class!='inActiveTD weekend']")

        # Select the departure date
        for date in all_dates:
            if date.get_attribute("data-date") == "24/08/2021":
                date.click()
                break


        # Click on flight search button
        self.driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
        time.sleep(4)



        # to handle dynamic scroll
        # Select the filter 1 stop

        # to handle dynamic scroll
        pageLength = self.driver.excute_script(
            "window.scrollTo(0, document.boday.scrollHeight);var pageLength=document.body.scrollHeight")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(2)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.boday.scrollHeight);var pageLength=document.body.scrollHeight" )
            if lastCount == pageLength:
                match = True

        time.sleep(4)

        # Select the filter 1 stop
        self.driver.find_element(By.XPATH, "//p[@class='font-lightgrey bold'][normailize-space()='1']").click()
        time.sleep(4)
        allstops1 = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
            "//span[contains(text(), 'Non Stop') or contains(text(), '1 Stop') or contains(text(), '2 Stop')]")))
        print(len(allstops1))


        # Verify that filtered results show flights having only 1 stop
        for stop in allstops1:
            print("The text is: " + stop.text)
            assert stop.text == "1 Stop"
            print("assert pass")
















test = TestSearchAndVerifyFilter()
test.test_search_flights()


