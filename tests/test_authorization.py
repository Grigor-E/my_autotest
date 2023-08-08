import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import Login_page


@pytest.mark.run(order=1)
def test_authorization(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(options=options)
    print("Start Test authorization")

    lp = Login_page(driver)
    lp.authorization()

    print("Finish Test authorization")
    driver.quit()

