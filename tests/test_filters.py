import time
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import Main_page
from pages.motorboats_page import Motorboats_page
from pages.rowboats_page import Rowboats_page


@pytest.mark.run(order=5)
def test_filters_1(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(options=options)

    print("Start Test 1")

    mp = Main_page(driver)
    mp.select_rowboats()

    rp = Rowboats_page(driver)
    rp.select_filters_rowboats()

    print("Finish Test 1")
    time.sleep(5)
    driver.quit()

@pytest.mark.run(order=4)
def test_filters_2(set_group, set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(options=options)

    print("Start Test 2")

    mp = Main_page(driver)
    mp.select_motorboats()

    rp = Motorboats_page(driver)
    rp.select_filters_motorboats()

    print("Finish Test 2")
    time.sleep(5)
    driver.quit()