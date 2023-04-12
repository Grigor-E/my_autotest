from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Motors_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    select_product_2 = "//*[@id='bx_3966226736_11929_362ce596257894d11ab5c1d73d13c755']/div[1]/div[3]/div[2]/div"  # локатор кнопки "Подробнее" товара №2 из группы товаров "Моторы"
    cart = "//*[@id='bx_basketFKauiI']/div/div[2]/a" # локатор перехода в корзину

    # Getters

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click select product 2")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    # Methods

    def select_products_2(self):
        self.get_current_url() # метод получения нашего url
        self.click_select_product_2() # метод нажатия кнопки выбора продукта 2
        self.click_cart() # метод перехода в корзину
