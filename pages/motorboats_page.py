import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Motorboats_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    slider_left = ".vue-slider-horizontal :nth-child(1) > .vue-slider-dot-handle" # локатор ползунка левого
    max_power = "//*[@class='row']/div[8]//i" # локатор выбора максимальной мощности двигателя
    power_forty = "//*[@class='row']/div[8]//div[9]/label/span" # локатор выбора мощности двигателя 40 л.с.
    show_button = ".bx-filter-parameters-box-container .btn_primary" # локатор кнопки "Показать"
    short_list = ".short_list.icon"  # выбор показа результата в виде short list icon

    # Getters

    def get_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.slider_left)))

    def get_max_power(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_power)))

    def get_power_forty(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.power_forty)))

    def get_show_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.show_button)))

    def get_short_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.short_list)))

    # Actions

    def click_max_power(self):
        self.get_max_power().click()
        print("Click max power")

    def click_power_forty(self):
        self.get_power_forty().click()
        print("Click power forty")

    def click_show_button(self):
        self.get_show_button().click()
        print("Click show button")

    def click_short_list(self):
        self.get_short_list().click()
        print("Click short list")

    # Methods

    def select_filters_motorboats(self):
        self.get_current_url() # метод получения нашего url
        self.assert_url('https://lodki-volga.ru/catalog/motornye_lodki/') # метод сравнения url
        self.action_slider_left(self.get_slider_left()) # метод action slider left из класса Base
        self.click_max_power() # метод нажатия кнопки выбора раздела максимальной мощности двигателя
        self.click_power_forty() # метод нажатия чекбокса выбора мощности двигателя 40 л.с.
        self.click_show_button()  # метод нажатия кнопки "Показать"
        self.click_short_list()  # метод нажатия кнопки показа результата в виде short list icon
        self.scroll()  # метод scroll из класса Base
        time.sleep(5)
        self.get_screenshot() # метод получения скриншота