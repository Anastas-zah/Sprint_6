import pytest
import allure
from urls import Urls
from pages.home_page import YaScooterHomePage
from pages.order_page import YaScooterOrderPage
from data import YaScooterOrderPageData as order_data


@allure.epic('Эпик_Создание заказа')
@allure.parent_suite('Parent_suite_Создание заказа')
class TestYaScooterOrderPage:
    @allure.suite('Suite_Заполнение данных на странице "Для кого самокат"')
    @allure.feature('Фича_Заполнения данных user-a при создании заказа на этапе "Для кого самокат"')
    @allure.story('Стори_Негативные проверки заполнения данных на этапе "Для кого самокат"')
    @allure.title('Ввод некорректного Имени')
    @allure.description('Проверка что при вводе некорректного имени в форме оформления заказа, выводится ошибка')
    def test_order_page_first_name_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.input_first_name('Вqw')
        ya_scooter_order_page.go_next()
        error_message_displayed = ya_scooter_order_page.is_first_name_error_displayed()
        assert error_message_displayed, "Ожидаемое сообщение об ошибке для некорректного имени не отображается."

    @allure.suite('Suite_Заполнение данных на странице "Для кого самокат"')
    @allure.feature('Фича_Заполнения данных user-a при создании заказа на этапе "Для кого самокат"')
    @allure.story('Стори_Негативные проверки заполнения данных на этапе "Для кого самокат"')
    @allure.title('Ввод некорректной Фамилии')
    @allure.description('Проверка что при вводе некорретной Фамилии в форме оформления заказа, выводится ошибка')
    def test_order_page_last_name_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.input_last_name('Вqw')
        ya_scooter_order_page.go_next()
        error_message_displayed = ya_scooter_order_page.is_last_name_error_displayed()
        assert error_message_displayed, "Ожидаемое сообщение об ошибке для некорректной фамилии не отображается."

    @allure.suite('Suite_Заполнение данных на странице "Для кого самокат"')
    @allure.feature('Фича_Заполнения данных user-a при создании заказа на этапе "Для кого самокат"')
    @allure.story('Стори_Негативные проверки заполнения данных на этапе "Для кого самокат"')
    @allure.title('Ввод Некорректного адреса')
    @allure.description('Проверка что при вводе некорретного адреса в форме оформление заказа, выводится ошибка')
    def test_order_page_address_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.input_address('Вqw')
        ya_scooter_order_page.go_next()
        error_message_displayed = ya_scooter_order_page.is_address_error_displayed()
        assert error_message_displayed, "Ожидаемое сообщение об ошибке для некорректного адреса не отображается."

    @allure.suite('Suite_Заполнение данных на странице "Для кого самокат"')
    @allure.feature('Фича_Заполнения данных user-a при создании заказа на этапе "Для кого самокат"')
    @allure.story('Стори_Негативные проверки заполнения данных на этапе "Для кого самокат"')
    @allure.title('Ввод пустого поля метро')
    @allure.description('Проверка что при пустом поле "Метро" в форме оформление заказа, выводится ошибка')
    def test_order_page_subway_input_empty_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.go_next()
        error_message_displayed = ya_scooter_order_page.is_subway_error_displayed()
        assert error_message_displayed, "Ожидаемое сообщение об ошибке для пустого поля метро не отображается."

    @allure.suite('Suite_Заполнение данных на странице "Для кого самокат"')
    @allure.feature('Фича_Заполнения данных user-a при создании заказа на этапе "Для кого самокат"')
    @allure.story('Стори_Негативные проверки заполнения данных на этапе "Для кого самокат"')
    @allure.title('Ввод некоректного номера телефона')
    @allure.description('Проверка что при вводе некорретного номера телефона в форме оформления заказа, выводится ошибка')
    def test_order_page_telephone_number_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.input_telephone_number('Вqw')
        ya_scooter_order_page.go_next()
        error_message_displayed = ya_scooter_order_page.is_telephone_number_error_displayed()
        assert error_message_displayed, "Ожидаемое сообщение об ошибке для некорректного номера телефона не отображается."

    @allure.suite('Suite_Заполнение данных на странице "Для кого самокат"')
    @allure.feature('Фича_Заполнения данных user-a при создании заказа на этапе "Для кого самокат"')
    @allure.story('Стори_Корректный ввод данных user-a на этапе "Для кого самокат"')
    @allure.title('Заполнение данных и переход с этапа "Для кого самокат" на этап "Про аренду"')
    @allure.description('Проверка что при корректных заполненных данных на этапе "Для кого самокат", '
                        'нажатии "Далее" происходит переход на следующий этап "Про аренду"')
    def test_order_page_go_to_choose_scooter_user_data_correct_open_about_rent(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.fill_user_data(order_data.data_sets['data_set1'])
        ya_scooter_order_page.go_next()
        order_button_visible = ya_scooter_order_page.is_order_button_visible()
        assert order_button_visible, "Кнопка заказа не отображается при корректных данных пользователя."

    @allure.suite('Suite_Заполнение данных на странице "Про аренду"')
    @allure.feature('Фича_Заполнения данных user-a при создании заказа на этапе "Про аренду"')
    @allure.story('Стори_Корректный ввод данных user-a на этапе "Про аренду"')
    @allure.title('Заполнение данных на этапе "Про аренду" и оформление заказа')
    @allure.description('Проверка что при корреткных заполненных данных на этапе "Про аренду", '
                        'нажатии на кнопку "Заказать", происходит оформление заказа, открывается модальное окно '
                        'с подтверждением об успешном создании заказа и присвоенным номером')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_about_rent_input_correct_data_and_order_show_order_number(self, driver, data_set):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.fill_user_data(order_data.data_sets[data_set])
        ya_scooter_order_page.go_next()
        ya_scooter_order_page.fill_rent_data(order_data.data_sets[data_set])
        ya_scooter_order_page.click_order()
        ya_scooter_order_page.click_accept_order()
        order_info_visible = ya_scooter_order_page.is_order_completed()
        assert order_info_visible, "Информация о завершении заказа должна быть видима"

    @allure.suite('Suite_Полный путь создания заказа')
    @allure.feature('Фича_Полный путь создания заказа')
    @allure.story('Стори_Оформление заказа и просмотр страницы заказа')
    @allure.title('Оформление заказа и переход на страницу с заказом')
    @allure.description('Проверка что при успешном оформлении заказа, заказ отображается на странице "Статус заказа" ')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_create_order_and_go_order_status(self, driver, data_set):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.fill_user_data(order_data.data_sets[data_set])
        ya_scooter_order_page.go_next()
        ya_scooter_order_page.fill_rent_data(order_data.data_sets[data_set])
        ya_scooter_order_page.click_order()
        ya_scooter_order_page.click_accept_order()
        order_number = ya_scooter_order_page.get_order_number()
        ya_scooter_order_page.click_go_to_status()
        current_url = ya_scooter_order_page.current_url()
        assert (Urls.ORDER_STATUS_PAGE in current_url) and (order_number in current_url)
