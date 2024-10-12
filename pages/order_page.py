import re
from pages.base_page import BasePage
from locators import YaScooterOrderPageLocator as Locators
import allure
from selenium.common.exceptions import NoSuchElementException


class YaScooterOrderPage(BasePage):

    @allure.step('Ввод фамилии')
    def input_last_name(self, last_name: str):
        """Ввод фамилии в поле."""
        self.find_element(Locators.LAST_NAME_INPUT).send_keys(last_name)
        return self

    @allure.step('Ввод имени')
    def input_first_name(self, first_name: str):
        """Ввод имени в поле."""
        self.find_element(Locators.FIRST_NAME_INPUT).send_keys(first_name)
        return self

    @allure.step('Ввод адреса')
    def input_address(self, address: str):
        """Ввод адреса в поле."""
        self.find_element(Locators.ADDRESS_INPUT).send_keys(address)
        return self

    @allure.step('Выбор метро')
    def choose_subway(self, subway_name: str):
        """Выбор метро."""
        self.find_element(Locators.SUBWAY_FIELD).click()
        self.find_element(Locators.SUBWAY_HINT_BUTTON(subway_name)).click()
        return self

    @allure.step('Ввод номера телефона')
    def input_telephone_number(self, telephone_number: str):
        """Ввод номера телефона в поле."""
        self.find_element(Locators.TELEPHONE_NUMBER_FIELD).send_keys(telephone_number)
        return self

    @allure.step('Перейти на следующий этап заказа')
    def go_next(self):
        """Переход на следующий этап заказа."""
        self.find_element(Locators.NEXT_BUTTON).click()
        return self

    @allure.step('Ввод даты')
    def input_date(self, date: str):
        """Ввод даты в поле."""
        self.find_element(Locators.DATE_FIELD).send_keys(date)
        return self

    @allure.step('Выбор периода аренды')
    def choose_rental_period(self, option: int):
        """Выбор периода аренды по индексу."""
        self.find_element(Locators.RENTAL_PERIOD_FIELD).click()
        self.find_elements(Locators.RENTAL_PERIOD_LIST)[option].click()
        return self

    @allure.step('Выбор цвета')
    def choose_color(self, option: list):
        """Выбор цвета по индексам из списка."""
        for idx in option:
            self.find_elements(Locators.COLOR_CHECKBOXES)[idx].click()
        return self

    @allure.step('Комментарий для курьера')
    def input_comment(self, comment_text: str):
        """Ввод комментария для курьера."""
        self.find_element(Locators.COMMENT_FOR_COURIER_FIELD).send_keys(comment_text)
        return self

    @allure.step('Нажать "Заказать"')
    def click_order(self):
        """Клик по кнопке 'Заказать'."""
        self.find_element(Locators.ORDER_BUTTON).click()
        return self

    @allure.step('Подтвердить заказ')
    def click_accept_order(self):
        """Клик по кнопке подтверждения заказа."""
        self.find_element(Locators.ACCEPT_ORDER_BUTTON).click()
        return self

    @allure.step('Вычитать номер заказа')
    def get_order_number(self):
        """Получение номера заказа из текста."""
        about_order_text = self.find_element(Locators.ORDER_COMPLETED_INFO).text
        return ''.join(re.findall('[0-9]', about_order_text))

    @allure.step('Перейти к статусу заказа')
    def click_go_to_status(self):
        """Переход к статусу заказа."""
        self.find_element(Locators.SHOW_STATUS_BUTTON).click()
        return self

    @allure.step('Заполнить данные на этапе "Для кого самокат"')
    def fill_user_data(self, data_set: dict):
        """Заполнение пользовательских данных."""
        return (self.input_first_name(data_set['first_name'])
                .input_last_name(data_set['last_name'])
                .input_address(data_set['address'])
                .choose_subway(data_set['subway_name'])
                .input_telephone_number(data_set['telephone_number']))

    @allure.step('Заполнить данные на этапе "Про аренду"')
    def fill_rent_data(self, data_set: dict):
        """Заполнение данных на этапе аренды."""
        return (self.input_date(data_set['date'])
                .choose_rental_period(data_set['rental_period'])
                .input_comment(data_set['comment_for_courier'])
                .choose_color(data_set['color']))

    def is_error_displayed(self, locator):
        """Проверка отображения ошибки по локатору."""
        try:
            return self.find_element(locator).is_displayed()
        except NoSuchElementException:
            return False

    @allure.step
    def is_first_name_error_displayed(self):
        """Проверка отображения ошибки для фамилии."""
        return self.is_error_displayed(Locators.INCORRECT_FIRST_NAME_MESSAGE)

    @allure.step
    def is_last_name_error_displayed(self):
        """Проверка отображения ошибки для имени."""
        return self.is_error_displayed(Locators.INCORRECT_LAST_NAME_MESSAGE)

    @allure.step
    def is_address_error_displayed(self):
        """Проверка отображения ошибки для адреса."""
        return self.is_error_displayed(Locators.INCORRECT_ADDRESS_MESSAGE)

    @allure.step
    def is_subway_error_displayed(self):
        """Проверка отображения ошибки для метро."""
        return self.is_error_displayed(Locators.INCORRECT_SUBWAY_MESSAGE)

    @allure.step
    def is_telephone_number_error_displayed(self):
        """Проверка отображения ошибки для номера телефона."""
        return self.is_error_displayed(Locators.INCORRECT_TELEPHONE_NUMBER_MESSAGE)

    @allure.step
    def is_order_button_visible(self):
        """Проверка видимости кнопки 'Заказать'."""
        return len(self.find_elements(Locators.ORDER_BUTTON)) > 0

    @allure.step('Проверка завершения заказа')
    def is_order_completed(self):
        """Проверка успешного завершения заказа."""
        return len(self.find_elements(Locators.ORDER_COMPLETED_INFO)) > 0