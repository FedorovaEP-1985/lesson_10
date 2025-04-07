from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from shop_page import ShopPage
import allure


@allure.feature("Тестирование интернет-магазина")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Полный цикл покупки товара")
@allure.description("""
Тест проверяет полный цикл покупки:
1. Авторизация пользователя
2. Добавление товара в корзину
3. Оформление заказа
4. Проверка итоговой суммы
""")


def test_shop_page():
    with allure.step("Инициализация драйвера и открытие страницы"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager(
            ).install()))
        shop_page = ShopPage(driver)

    with allure.step("Открытие главной страницы магазина"):
        shop_page.open()

    with allure.step("Авторизация пользователя"):
        shop_page.authorization()

    with allure.step("Добавить в корзину"):
        shop_page.add_to_cart()

    with allure.step("В корзине"):
        shop_page.in_cart()

    with allure.step("Начать оформление заказа"):
        shop_page.click_checkout()

    with allure.step("Заполнение данных для доставки"):
        shop_page.fill_form(
            first_name="Иван", last_name="Петров",
            postal_code="123456")

    with allure.step("Проверка итоговой суммы"):
        shop_page.checking_total_amount()

    with allure.step("Закрыть браузер"):
        driver.quit()
