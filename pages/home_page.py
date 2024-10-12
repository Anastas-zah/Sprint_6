import allure
from pages.base_page import BasePage
from locators import BasePageLocator
from locators import YaScooterHomePageLocator as Locators


class YaScooterHomePage(BasePage):

    @allure.step('Нажать на кнопку заказа вверху страницы')
    def click_top_order_button(self):
        self.click_element(Locators.TOP_ORDER_BUTTON)

    @allure.step('Нажать на кнопку заказа внизу страницы')
    def click_bottom_order_button(self):
        self.click_element(Locators.BOTTOM_ORDER_BUTTON)

    @allure.step('Нажать на вопрос в FAQ')
    def click_faq_question(self, question_number: int):
        elems = self.find_elements(Locators.FAQ_BUTTONS, 10)
        if question_number < 0 or question_number >= len(elems):
            raise ValueError("Invalid question number")
        elems[question_number].click()

    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        self.switch_to_window(window_number)

    @allure.step('Перейти на страницу яндекса')
    def click_yandex_button(self):
        self.click_element(BasePageLocator.YANDEX_SITE_BUTTON)

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        self.click_element(BasePageLocator.COOKIE_ACCEPT_BUTTON)