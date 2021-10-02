from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors


"""
This pytest test was automatically generated by TestProject
    Project: Hans' Project
    Package: TestProject.Generated.Tests.HansProject
    Test: Assign an officer to first dispatch
    Generated by: Hans Hwang (hhwang@d3security.com)
    Generated on 10/02/2021, 00:09:41
"""


@report_assertion_errors
def test_main(driver):
    """Dispatch Operations Center."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://gsstage.d3securityonline.com/QA/VSOC/Login.aspx"
    DispatchIDtype = ""
    DispatchID = ""

    # 1. Click 'dispatch center first row - 1727'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'FrameOnLifeServer']|//*[@name = 'FrameOnLifeServer']|/html/body/form/iframe"))
    dispatch_center_first_row_1727 = driver.find_element(By.XPATH,
                                                         "//div[1]/div[1]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]")
    dispatch_center_first_row_1727.click()

    # 2. Click 'Selected Dispatch'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'FrameOnLifeServer']|//*[@name = 'FrameOnLifeServer']|/html/body/form/iframe"))
    selected_dispatch = driver.find_element(By.XPATH,
                                            "//a[3][. = 'Selected Dispatch']")
    selected_dispatch.click()

    # 3. Click 'OnDuty Officers 1st row - TD'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'FrameOnLifeServer']|//*[@name = 'FrameOnLifeServer']|/html/body/form/iframe"))
    onduty_officers_1st_row_td = driver.find_element(By.XPATH,
                                                     "//div[2]/div[1]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]")
    onduty_officers_1st_row_td.click()

    # 4. Click 'Assign'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'FrameOnLifeServer']|//*[@name = 'FrameOnLifeServer']|/html/body/form/iframe"))
    assign = driver.find_element(By.CSS_SELECTOR,
                                 "#assign")
    assign.click()

    # 5. Click 'OK'
    step_settings = StepSettings(always_pass=True)
    with DriverStepSettings(driver, step_settings):
        ok = driver.find_element(By.XPATH,
                                 "//button[. = 'OK']")
        ok.click()

    # 6. Click 'Save3'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'FrameOnLifeServer']|//*[@name = 'FrameOnLifeServer']|/html/body/form/iframe"))
    save3 = driver.find_element(By.CSS_SELECTOR,
                                "#dsp_toolbar_saveExisting")
    save3.click()
