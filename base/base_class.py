import datetime
from selenium.webdriver import ActionChains

class Base():

    def __init__(self, driver):
        self.driver = driver

    # Method get current url

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url" + get_url)

    # Method assert word

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    # Method screenshot

    def get_screenshot(self): # делается скриншот страницы результата
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\PycharmProjects\\main_start_project\\screen\\' + name_screenshot)

    # Method assert url

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    # Method action slider right

    def action_slider_right(self, slider_right):
        action = ActionChains(self.driver)
        action.click_and_hold(slider_right).move_by_offset(-180,0).release().perform()
        print("Good action slider right")

    # Method action slider left

    def action_slider_left(self, slider_left):
        action = ActionChains(self.driver)
        action.click_and_hold(slider_left).move_by_offset(20, 0).release().perform()
        print("Good action slider left")

    # Method scroll

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0,500)")
        print("Good scroll")