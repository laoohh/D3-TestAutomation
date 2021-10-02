import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)

    def page_scroll(self):
        # to handle dynamic scroll
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(3)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;" )
            if lastCount == pageLength:
                match = True

        time.sleep(2)


    def wait_for_presence_of_all_elements(self, locator_type, locator):
        list_of_elements = self.wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self, locator_type, locator):
        element = self.wait.until(EC.element_to_be_clickable((locator_type,locator)))
        return element



