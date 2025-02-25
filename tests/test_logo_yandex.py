import allure
from conftest import driver
from constants import Constants
from pages.main_page import MainPage


class TestLogoYandex:
    @allure.title("Тестирование логотипа Яндекс/ Переход на Дзен")
    def test_logo_yandex(self, driver):
        yandex = MainPage(driver)
        yandex.get_url(Constants.URL)
        yandex.click_switch_window(1)
        assert yandex.check_url(Constants.URL_DZEN)
