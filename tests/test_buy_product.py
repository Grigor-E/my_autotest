import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from pages.boat_accessories_page import Boat_accessories_page
from pages.basket_page import Basket_page
from pages.finish_page import Finish_page
from pages.main_page import Main_page
from pages.motors_page import Motors_page
# from pages.tourism_page import Tourism_page

@pytest.mark.run(order=3)
def test_buy_product_1(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(options=options)
    print("Start Test 1")

    mp = Main_page(driver)
    mp.select_boat_accessories()

    ba = Boat_accessories_page(driver)
    ba.select_products_1()

    bp = Basket_page(driver)
    bp.product_confirmation()

    fp = Finish_page(driver)
    fp.ordering()
    fp.finish()

    print("Finish Test 1")
    driver.quit()

@pytest.mark.run(order=2)
def test_buy_product_2(set_group, set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(options=options)

    print("Start Test 2")

    mp = Main_page(driver)
    mp.select_motors()

    mop = Motors_page(driver)
    mop.select_products_2()

    bp = Basket_page(driver)
    bp.back_to_product_selection()

    print("Finish Test 2")
    driver.quit()

# @pytest.mark.run(order=2)
# def test_buy_product_3(set_up):
#     options = Options()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     driver = webdriver.WebDriver(options=options)
#
#     print("Start Test 3")
#
#     mp = Main_page(driver)
#     mp.select_tourism()
#
#     tp = Tourism_page(driver)
#     tp.select_products_3()
#
#     bp = Basket_page(driver)
#     bp.product_confirmation()
#
#     fp = Finish_page(driver)
#     fp.finish()
#
#     print("Finish Test 3")
#     driver.quit()