import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Rowboats_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    slider_right = ".vue-slider-horizontal :nth-child(2) > .vue-slider-dot-handle" # локатор ползунка правого
    brand = "//*[@class='row']/div[2]//i" # локатор выбора бренда
    brand_akva = "//*[@class='row']/div[2]//div[1]/label/span" # локатор выбора бренда "Аква"
    brand_musson = "//*[@class='row']/div[2]//div[3]/label/span" # локатор выбора бренда "Мусон"
    length = "//*[@class='row']/div[4]//i" # локатор выбора длины
    length_first = "//*[@class='row']/div[4]//div[1]/label/span" # локатор первой по очередности длины
    length_second = "//*[@class='row']/div[4]//div[2]/label/span"  # локатор второй по очередности длины
    capacity = "//*[@class='row']/div[6]//i" # локатор выбора вместимости
    capacity_first = "//*[@class='row']/div[6]//div[1]/label/span" # локатор выбора вместимости на одного человека
    balloon_diameter = "//*[@class='row']/div[8]//i"  # локатор выбора диаметра баллона
    diameter_first = "//*[@class='row']/div[8]//div[1]/label/span" # локатор диаметра баллона первого по очередности
    diameter_third = "//*[@class='row']/div[8]//div[3]/label/span"  # локатор диаметра баллона третьего по очередности
    bottom_type = "//*[@class='row']/div[10]//i" # локатор выбора типа дна
    stretch_bottom = "//*[@class='row']/div[10]//div[2]/label/span" # локатор натяжного типа дна
    show_button = ".bx-filter-parameters-box-container .btn_primary" # локатор кнопки "Показать"

    # Getters

    def get_slider_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.slider_right)))

    def get_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand)))

    def get_brand_akva(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_akva)))

    def get_brand_musson(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_musson)))

    def get_length(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.length)))

    def get_length_first(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.length_first)))

    def get_length_second(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.length_second)))

    def get_capacity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.capacity)))

    def get_capacity_first(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.capacity_first)))

    def get_balloon_diameter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.balloon_diameter)))

    def get_diameter_first(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.diameter_first)))

    def get_diameter_third(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.diameter_third)))

    def get_bottom_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bottom_type)))

    def get_stretch_bottom(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.stretch_bottom)))

    def get_show_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.show_button)))

    # Actions

    def click_brand(self):
        self.get_brand().click()
        print("Click brand")

    def click_brand_akva(self):
        self.get_brand_akva().click()
        print("Click brand akva")

    def click_brand_musson(self):
        self.get_brand_musson().click()
        print("Click brand musson")

    def click_length(self):
        self.get_length().click()
        print("Click length")

    def click_length_first(self):
        self.get_length_first().click()
        print("Click length first")

    def click_length_second(self):
        self.get_length_second().click()
        print("Click length second")

    def click_capacity(self):
        self.get_capacity().click()
        print("Click capacity")

    def click_capacity_first(self):
        self.get_capacity_first().click()
        print("Click capacity first")

    def click_balloon_diameter(self):
        self.get_balloon_diameter().click()
        print("Click balloon diameter")

    def click_diameter_first(self):
        self.get_diameter_first().click()
        print("Click diameter first")

    def click_diameter_third(self):
        self.get_diameter_third().click()
        print("Click diameter third")

    def click_bottom_type(self):
        self.get_bottom_type().click()
        print("Click bottom type")

    def click_stretch_bottom(self):
        self.get_stretch_bottom().click()
        print("Click stretch bottom")

    def click_show_button(self):
        self.get_show_button().click()
        print("Click show button")

    # Methods

    def select_filters_rowboats(self):
        self.get_current_url() # метод получения нашего url
        self.assert_url('https://lodki-volga.ru/catalog/grebnye_lodki/') # метод сравнения url
        self.action_slider_right(self.get_slider_right()) # метод action slider right из класса Base
        self.click_brand() # метод нажатия кнопки выбора бренда
        self.click_brand_akva() # метод нажатия чекбокса выбора бренда "Аква"
        self.click_brand_musson() # метод нажатия чекбокса выбора бренда "Муссон"
        self.click_length() # метод нажатия кнопки выбора длины
        self.click_length_first() # метод нажатия чекбокса первой по очередности длины
        self.click_length_second() # метод нажатия чекбокса второй по очередности длины
        self.click_capacity() # метод нажатия кнопки выбора вместимости
        self.click_capacity_first() # метод нажатия чекбокса выбора вместимости на одного человека
        self.click_balloon_diameter() # метод нажатия кнопки выбора диаметра баллона
        self.click_diameter_first() # метод нажатия чекбокса диаметра баллона первого по очередности
        self.click_diameter_third() # метод нажатия чекбокса диаметра баллона третьего по очередности
        self.click_bottom_type() # метод нажатия кнопки выбора типа дна
        self.click_stretch_bottom() # метод нажатия чекбокса выбора натяжного типа дна
        self.click_show_button() # метод нажатия кнопки "Показать"
        self.scroll() # метод scroll из класса Base
        time.sleep(5)
        self.get_screenshot() # метод получения скриншота