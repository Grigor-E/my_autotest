from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Login_page(Base): # класс потомок класса Base

    url = 'https://lodki-volga.ru/personal/' # адрес сайта Лодки Поволжья

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    user_name = "//input[@id='USER_LOGIN']" # локатор поля ввода "Логин или email*"
    password = "//input[@type='password']" # локатор поля ввода пароля
    remember = "//div[@class='remember_me checked']" # локатор функции "Запомнить меня на этом устройстве"
    login_button = "//button[@class='btn btn_big btn_primary']" # локатор кнопки Войти
    main_word = "//html/body/div[2]/header/div[2]/div/div/div[2]/div/a/div/div[2]/div[1]"

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_remember(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.remember)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.main_word)))

    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_remember(self):
        self.get_remember().click()
        print("Click remember")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods

    def autorization(self):
        self.driver.get(self.url) # метод октрытия страницы
        self.driver.maximize_window() # метод открытия во весь экран
        self.get_current_url() # метод получения нашего url
        self.input_user_name("УКАЖИТЕ СВОЙ @mail.ru") # метод заполнения поля логина
        self.input_password("УКАЖИТЕ СВОЙ") # метод заполнения поля пароля
        self.click_remember()  # метод cнятия галочки функции "Запомнить меня на этом устройстве"
        self.click_login_button() # метод нажатия кнопки "Вход"
        self.assert_word(self.get_main_word(), '8 (800) 770 01 51') # метод сравнения текста