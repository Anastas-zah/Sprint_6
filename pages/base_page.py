import allure
from urls import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(locator))
        element.click()

    def switch_to_window(self, window_number: int):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_url_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))

    @allure.step('Перейти по адресу')
    def go_to_site(self, url=None):
        if url is None:
            url = Urls.MAIN_PAGE
        self.driver.get(url)

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url
