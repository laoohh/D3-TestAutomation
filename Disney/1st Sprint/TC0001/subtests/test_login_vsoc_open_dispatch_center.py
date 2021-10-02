from selenium.webdriver.common.by import By
from src.testproject.decorator import report_assertion_errors
import project_parameters


"""
This pytest test was automatically generated by TestProject
    Project: Hans' Project
    Package: TestProject.Generated.Tests.HansProject
    Test: Login VSOC - Open Dispatch Center
    Generated by: Hans Hwang (hhwang@d3security.com)
    Generated on 10/02/2021, 00:09:41
"""


@report_assertion_errors
def test_main(driver):
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://gsstage.d3securityonline.com/QA/VSOC/Login.aspx"
    Username = "hans"
    Password = "D1sney2020!"

    # 1. Navigate to '{project_parameters.ApplicationURL4GsStateQAvSOC}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{project_parameters.ApplicationURL4GsStateQAvSOC}')

    # 2. Is 'Username1' visible?
    username1 = driver.find_element(By.XPATH,
                                    "//label[. = 'Username']")
    assert username1.is_displayed()

    # 3. Click 'username'
    username = driver.find_element(By.CSS_SELECTOR,
                                   "#username")
    username.click()

    # 4. Type '{Username}' in 'username'
    username = driver.find_element(By.CSS_SELECTOR,
                                   "#username")
    username.send_keys(f'{Username}')

    # 5. Click 'password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#password")
    password.click()

    # 6. Type '{Password}' in 'password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#password")
    password.send_keys(f'{Password}')

    # 7. Click 'Button_Login'
    button_login = driver.find_element(By.CSS_SELECTOR,
                                       "#Button_Login")
    button_login.click()

    # 8. Switch to window '1'
    driver.switch_to.window(driver.window_handles[1])

    # 9. Is 'hamburgerOpen' is clickable?
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'FrameOnLifeServer']|//*[@name = 'FrameOnLifeServer']|/html/body/form/iframe"))
    hamburgeropen = driver.find_element(By.CSS_SELECTOR,
                                        "#hamburgerOpen")
    assert hamburgeropen.is_enabled()

    # 10. Click 'hamburgerOpen'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'FrameOnLifeServer']|//*[@name = 'FrameOnLifeServer']|/html/body/form/iframe"))
    hamburgeropen = driver.find_element(By.CSS_SELECTOR,
                                        "#hamburgerOpen")
    hamburgeropen.click()

    # 11. Click 'More'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'FrameOnLifeServer']|//*[@name = 'FrameOnLifeServer']|/html/body/form/iframe"))
    more = driver.find_element(By.XPATH,
                               "//span[. = 'More']")
    more.click()

    # 12. Click 'Dispatches'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'FrameOnLifeServer']|//*[@name = 'FrameOnLifeServer']|/html/body/form/iframe"))
    dispatches = driver.find_element(By.XPATH,
                                     "//span[. = 'Dispatches']")
    dispatches.click()

    # 13. Click 'Dispatch Operations Center1'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'FrameOnLifeServer']|//*[@name = 'FrameOnLifeServer']|/html/body/form/iframe"))
    dispatch_operations_center1 = driver.find_element(By.XPATH,
                                                      "//li[3]/a[. = 'Dispatch Operations Center']")
    dispatch_operations_center1.click()

    # 14. Is 'Active Dispatches (696)' visible?
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'FrameOnLifeServer']|//*[@name = 'FrameOnLifeServer']|/html/body/form/iframe"))
    active_dispatches_696_ = driver.find_element(By.XPATH,
                                                 "//div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")
    assert active_dispatches_696_.is_displayed()
