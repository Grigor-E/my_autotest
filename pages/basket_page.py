from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Basket_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    button_go_to_shopping = "btn_secondary"  # локатор кнопки "Перейти к покупкам"
    order_button = ".order_items :nth-child(2) > .btn" # локатор кнопки "Оформить заказ"

    # Getters

    def get_button_go_to_shopping(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.button_go_to_shopping)))
    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.order_button)))

    # Actions

    def click_button_go_to_shopping(self):
        self.get_button_go_to_shopping().click()
        print("Click button go to shopping")

    def click_order_button(self):
        self.get_order_button().click()
        print("Click order button")

    # Methods

    def back_to_product_selection(self):
        self.get_current_url()  # метод получения нашего url
        self.click_button_go_to_shopping() # метод нажатия кнопки "Перейти к покупкам"
        self.get_current_url()  # метод получения нашего url
        self.assert_url('https://lodki-volga.ru/Yoshkar-ola/catalog/')  # метод сравнения url

    def product_confirmation(self):
        self.get_current_url() # метод получения нашего url
        self.click_order_button() # метод нажатия кнопки "Оформить заказ" в корзине
