from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Motors_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    count_elements_link = "count_elements_link" # локатор выбора количества отображаемых товаров на странице
    count_elements = "[data-count='48']"  # локатор количества равного 48 отображаемых товаров на странице
    select_product_2 = "#bx_3966226736_15088_b11dbf01adecda9113ee4e30d77829df :nth-child(1) > .item_buy_link"  # локатор кнопки "Подробнее" товара из группы товаров "Моторы"
    link_to_basket = "basket_link"  # локатор ссылки на корзину

    # Getters

    def get_count_elements_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.count_elements_link)))

    def get_count_elements(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.count_elements)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_product_2)))

    def get_link_to_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.link_to_basket)))

    # Actions

    def click_count_elements_link(self):
        self.get_count_elements_link().click()
        print("Click count elements link")

    def click_count_elements(self):
        self.get_count_elements().click()
        print("Click count elements")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click select product 2")

    def click_link_to_basket(self):
        self.get_link_to_basket().click()
        print("Click link to basket")

    # Methods

    def select_products_2(self):
        self.get_current_url() # метод получения нашего url
        self.click_count_elements_link() # метод нажатия на список количества отображаемых товаров на странице
        self.click_count_elements()  # метод нажатия на количество равное 48 отображаемых товаров на странице
        self.click_select_product_2() # метод нажатия кнопки выбора товара
        self.click_link_to_basket()  # метод нажатия ссылки на страницу корзины
