from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    rowboats = ".container :nth-child(1) > .section-tabs__link" # локатор выбора списка гребных лодок
    motorboats = ".container :nth-child(2) > .section-tabs__link" # локатор выбора списка моторных лодок
    boat_accessories = ".container :nth-child(3) > .section-tabs__link" # локатор выбора списка комплектующих для лодок
    motors = ".container :nth-child(5) > .section-tabs__link" # локатор выбора списка моторов
    # tourism = "//*[@id='submenu_section_4']/a/span[3]" # локатор выбора списка товаров для туризма

    # Getters

    def get_rowboats(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.rowboats)))

    def get_motorboats(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.motorboats)))

    def get_boat_accessories(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.boat_accessories)))

    def get_motors(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.motors)))

    # def get_tourism(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tourism)))

    # Actions

    def click_rowboats(self):
        self.get_rowboats().click()
        print("Click select rowboats")

    def click_motorboats(self):
        self.get_motorboats().click()
        print("Click select motorboats")

    def click_boat_accessories(self):
        self.get_boat_accessories().click()
        print("Click select boat accessories")

    def click_motors(self):
        self.get_motors().click()
        print("Click select motors")

    # def click_tourism(self):
    #     self.get_tourism().click()
    #     print("Click select tourism")

    # Methods

    def select_rowboats(self):
        self.get_current_url()  # метод получения нашего url
        self.click_rowboats()  # метод нажатия кнопки выбора меню "Гребные лодки"

    def select_motorboats(self):
        self.get_current_url()  # метод получения нашего url
        self.click_motorboats()  # метод нажатия кнопки выбора меню "Моторные лодки"

    def select_boat_accessories(self):
        self.get_current_url() # метод получения нашего url
        self.click_boat_accessories() # метод нажатия кнопки выбора меню "Комплектующие для лодок"

    def select_motors(self):
        self.get_current_url() # метод получения нашего url
        self.click_motors() # метод нажатия кнопки выбора меню "Моторы"

    # def select_tourism(self):
    #     self.get_current_url() # метод получения нашего url
    #     self.click_tourism() # метод нажатия кнопки выбора меню "Туризм"