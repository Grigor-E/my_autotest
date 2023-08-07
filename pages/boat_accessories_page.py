from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Boat_accessories_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    select_product_1 = "#bx_3966226736_16843_362ce596257894d11ab5c1d73d13c755 :nth-child(1) > .item_buy_link"  # локатор кнопки "Купить" товара №1 (Помпа сушительная) из группы товаров "Комплектующие для лодок"
    price_product_1 = "#bx_3966226736_16843_362ce596257894d11ab5c1d73d13c755 :nth-child(1) > .price"  # локатор цены товара №1 (Помпа сушительная) из группы товаров "Комплектующие для лодок"
    link_to_basket = "basket_link" #  локатор ссылки на корзину
    button_go_to_basket = ".popup_wr :nth-child(2) > .btn"  # локатор кнопки "Перейти в корзину"

    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_product_1)))

    def get_price_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.price_product_1)))

    def get_link_to_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.link_to_basket)))

    def get_button_go_to_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.button_go_to_basket)))

    # Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click select product 1")

    def click_link_to_basket(self):
        self.get_link_to_basket().click()
        print("Click link to basket")

    def click_button_go_to_basket(self):
        self.get_button_go_to_basket().click()
        print("Click button go to basket")

    def value_price_product_1(self):
        word_price_1 = self.get_price_product_1()
        value_price_1 = word_price_1.text
        print(value_price_1 + " - price product 1")

    # Methods

    def select_products_1(self):
        self.get_current_url() # метод получения нашего url
        self.click_select_product_1() # метод нажатия кнопки выбора товара №1 (нумерация в тесте, а не на странице)
        self.value_price_product_1() # метод получения и печати текста цены выбранного товара
        self.click_link_to_basket() # метод нажатия ссылки на корзину
        self.click_button_go_to_basket() # метод нажатия кнопки "Перейти в корзину"