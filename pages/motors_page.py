from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Motors_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    select_product_2 = "#bx_3966226736_15089_1a358e4c7511fb2753fa0770e1da3fb4 :nth-child(1) > .item_buy_link"  # локатор кнопки "Подробнее" товара из группы товаров "Моторы"
    link_to_basket = "basket_link"  # локатор ссылки на корзину
    button_go_to_basket = ".popup_wr :nth-child(2) > .btn"  # локатор кнопки "Перейти в корзину"

    # Getters

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_product_2)))

    def get_link_to_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.link_to_basket)))

    def get_button_go_to_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.button_go_to_basket)))

    # Actions

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click select product 2")

    def click_link_to_basket(self):
        self.get_link_to_basket().click()
        print("Click link to basket")

    def click_button_go_to_basket(self):
        self.get_button_go_to_basket().click()
        print("Click button go to basket")

    # Methods

    def select_products_2(self):
        self.get_current_url() # метод получения нашего url
        self.click_select_product_2() # метод нажатия кнопки выбора товара
        self.click_link_to_basket()  # метод нажатия ссылки на корзину
        self.click_button_go_to_basket()  # метод нажатия кнопки "Перейти в корзину"
