# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from base.base_class import Base

#
# class Tourism_page(Base):
#
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     # Locators
#
#     select_product_3 = "//*[@id='bx_3966226736_46344_c80764dfaf26ca80162484593ec7c29b']/div[1]/div[3]/div[2]/div" # локатор кнопки "Подробнее" товара №3 из группы товаров "Туризм"
#     link_to_basket = "basket_link"  # локатор ссылки на корзину
#     button_go_to_basket = ".popup_wr :nth-child(2) > .btn"  # локатор кнопки "Перейти в корзину"
#
#     # Getters
#
#     def get_select_product_3(self):
#         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))
#
#     def get_link_to_basket(self):
#         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.link_to_basket)))
#
#     def get_button_go_to_basket(self):
#         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.button_go_to_basket)))
#
#     # Actions
#
#     def click_select_product_3(self):
#         self.get_select_product_3().click()
#         print("Click select product 3")
#
#     def click_link_to_basket(self):
#         self.get_link_to_basket().click()
#         print("Click link to basket")
#
#     def click_button_go_to_basket(self):
#         self.get_button_go_to_basket().click()
#         print("Click button go to basket")
#
#     # Methods
#
#     def select_products_3(self):
#         self.get_current_url() # метод получения нашего url
#         self.click_select_product_3() # метод нажатия кнопки выбора продукта 3
#         self.click_link_to_basket()  # метод нажатия ссылки на страницу корзины
#         self.click_button_go_to_basket()  # метод нажатия кнопки "Перейти в корзину"