from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Boat_accessories_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    select_product_1 = "//*[@id='bx_3966226736_47113_c80764dfaf26ca80162484593ec7c29b']/div/div[2]/div[2]/div"  # локатор кнопки "Купить" товара №1 из группы товаров "Комплектующие для лодок"
    price_product_1 = "//*[@id='bx_3966226736_47113_c80764dfaf26ca80162484593ec7c29b']/div/div[2]/div[1]/div"  # локатор цены товара №1 из группы товаров "Комплектующие для лодок"
    cart = "//*[@id='bx_basketFKauiI']/div/div[2]/a" # локатор перехода в корзину

    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_price_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.price_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click select product 1")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def value_price_product_1(self):
        word_price_1 = self.get_price_product_1()
        value_price_1 = word_price_1.text
        print(value_price_1 + " - price product 1")

    # Methods

    def select_products_1(self):
        self.get_current_url() # метод получения нашего url
        self.click_select_product_1() # метод нажатия кнопки выбора продукта 1
        self.value_price_product_1() # метод получения и печати текста цены выбранного товара
        self.click_cart() # метод перехода в корзину