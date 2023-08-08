import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    street = "street" # локатор ввода улицы при оформлении заказа
    house = "house" # локатор ввода дома при оформлении заказа
    price_product_one = ".product_item_content :nth-child(1) > .price" # локатор цены товара №1 (нумерация в тесте, а не на странице, где выбран товар) при оформлении заказа
    clear_button = "//*[@class='btn_group']/a[1]" # локатор кнопки очистки корзины
    delete_button = ".dg-btn-content" # локатор кнопки подтверждения удаления содержимого корзины

    # Getters

    def get_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, self.street)))

    def get_house(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, self.house)))

    def get_price_product_one(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.price_product_one)))

    def get_clear_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clear_button)))

    def get_delete_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.delete_button)))

    # Actions

    def input_street(self, street):
        self.get_street().send_keys(street)
        print("Input street")

    def input_house(self, house):
        self.get_house().send_keys(house)
        print("Input house")

    def click_clear_button(self):
        self.get_clear_button().click()
        print("Click clear button")

    def click_delete_button(self):
        self.get_delete_button().click()
        print("Click delete button")

    # Methods

    def ordering(self):
        self.get_current_url()  # метод получения нашего url
        self.assert_url('https://lodki-volga.ru/order/make/')  # метод сравнения url
        self.assert_word(self.get_price_product_one(), '1 690 ₽') # метод assert word для сравнения цены выбранного товара с ценой при оформлении заказа
        self.input_street("Пушкина")  # метод заполнения поля улицы
        self.input_house("Колотушкина")  # метод заполнения поля дома
        time.sleep(5)
        self.get_screenshot()  # метод получения скриншота

    def finish(self):
        self.driver.back() # метод возврата на страницу корзины
        self.get_current_url()  # метод получения нашего url
        self.assert_url('https://lodki-volga.ru/cart/')  # метод сравнения url
        self.click_clear_button() # метод нажатия кнопки "Очистить корзину"
        self.click_delete_button()  # метод подтверждения удаления содержимого корзины
        time.sleep(5)
        self.get_screenshot()  # метод получения скриншота