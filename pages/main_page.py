from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    url = 'https://lodki-volga.ru/'  # адрес сайта Лодки Поволжья

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    rowboats = ".container :nth-child(1) > .section-tabs__link" # локатор выбора гребных лодок
    rowboats_link = "#bx_3966226736_product_list_wfcism :nth-child(1) > .section_title_link" # локатор ссылки на список гребных лодок
    motorboats = ".container :nth-child(2) > .section-tabs__link" # локатор выбора моторных лодок
    motorboats_link = "#bx_1970176138_product_list_eiFvAd :nth-child(1) > .section_title_link"  # локатор ссылки на список моторных лодок
    boat_accessories = ".container :nth-child(3) > .section-tabs__link" # локатор выбора комплектующих для лодок
    boat_accessories_link = "#bx_40480796_product_list_U70oIE :nth-child(1) > .section_title_link"  # локатор ссылки на список комплектующих для лодок
    motors = ".container :nth-child(5) > .section-tabs__link" # локатор выбора списка моторов
    motors_link = "#bx_3943306537_product_list_FdmUJO :nth-child(1) > .section_title_link"  # локатор ссылки на список моторов
    # tourism = "//*[@id='submenu_section_4']/a/span[3]" # локатор выбора списка товаров для туризма

    # Getters

    def get_rowboats(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.rowboats)))

    def get_rowboats_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.rowboats_link)))

    def get_motorboats(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.motorboats)))

    def get_motorboats_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.motorboats_link)))

    def get_boat_accessories(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.boat_accessories)))

    def get_boat_accessories_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.boat_accessories_link)))

    def get_motors(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.motors)))

    def get_motors_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.motors_link)))

    # def get_tourism(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tourism)))

    # Actions

    def click_rowboats(self):
        self.get_rowboats().click()
        print("Click rowboats")

    def click_rowboats_link(self):
        self.get_rowboats_link().click()
        print("Click rowboats link")

    def click_motorboats(self):
        self.get_motorboats().click()
        print("Click motorboats")

    def click_motorboats_link(self):
        self.get_motorboats_link().click()
        print("Click motorboats link")

    def click_boat_accessories(self):
        self.get_boat_accessories().click()
        print("Click boat accessories")

    def click_boat_accessories_link(self):
        self.get_boat_accessories_link().click()
        print("Click boat accessories link")

    def click_motors(self):
        self.get_motors().click()
        print("Click motors")

    def click_motors_link(self):
        self.get_motors_link().click()
        print("Click motors link")

    # def click_tourism(self):
    #     self.get_tourism().click()
    #     print("Click tourism")

    # Methods

    def select_rowboats(self):
        self.driver.get(self.url)  # метод открытия страницы
        self.driver.maximize_window()  # метод открытия во весь экран
        self.get_current_url()  # метод получения нашего url
        self.click_rowboats()  # метод нажатия на меню "Гребные лодки"
        self.click_rowboats_link()  # метод нажатия на ссылку для перехода в меню "Гребные лодки"

    def select_motorboats(self):
        self.driver.get(self.url)  # метод открытия страницы
        self.driver.maximize_window()  # метод открытия во весь экран
        self.get_current_url()  # метод получения нашего url
        self.click_motorboats()  # метод нажатия на меню "Моторные лодки"
        self.click_motorboats_link()  # метод нажатия на ссылку для перехода в меню "Моторные лодки"

    def select_boat_accessories(self):
        self.driver.get(self.url)  # метод открытия страницы
        self.driver.maximize_window()  # метод открытия во весь экран
        self.get_current_url() # метод получения нашего url
        self.click_boat_accessories() # метод нажатия на меню "Комплектующие для лодок"
        self.click_boat_accessories_link()  # метод нажатия на ссылку для перехода в меню "Комплектующие для лодок"

    def select_motors(self):
        self.driver.get(self.url)  # метод открытия страницы
        self.driver.maximize_window()  # метод открытия во весь экран
        self.get_current_url() # метод получения нашего url
        self.click_motors() # метод нажатия на меню "Моторы"
        self.click_motors_link()  # метод нажатия на ссылку для перехода в меню "Моторы"

    # def select_tourism(self):
    # self.driver.get(self.url)  # метод открытия страницы
    # self.driver.maximize_window()  # метод открытия во весь экран
    #     self.get_current_url() # метод получения нашего url
    #     self.click_tourism() # метод нажатия на меню "Туризм"