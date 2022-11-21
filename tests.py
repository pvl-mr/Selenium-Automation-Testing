import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from random import randrange

BASE_URL = "http://localhost:3000"
AUTH_EMAIL = "mari**@mail.ru"
AUTH_PASS = "***"
class WebAppTests(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_add_portfolio(self):
        """Тест 1.1. Добавления портфеля"""
        driver = self.driver
        self.login()
        delay = 5
        random_name = f"portfolio {randrange(100)}"

        btn_to_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/header/nav/div/div/div[2]/div[1]/a[1]")))
        btn_to_portfolio.click()

        btn_add_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn-outline-primary")))
        btn_add_portfolio.click()
        time.sleep(2)
        input_name = driver.find_element(By.XPATH, "//html/body/div[3]/div/div/div[2]/div[1]/input")
        input_name.send_keys(random_name)
        input_months = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div[2]/input")
        input_months.send_keys(10)
        btn_add = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]")
        btn_add.click()

        time.sleep(5)

        assert random_name in driver.page_source

    def test_delete_portfolio(self):
        """Тест 1.2. Удаление портфеля"""
        driver = self.driver
        self.login()
        delay = 5

        btn_to_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/header/nav/div/div/div[2]/div[1]/a[1]")))
        btn_to_portfolio.click()

        time.sleep(5)

        assert "test_portfolio" not in driver.page_source

    def test_update_portfolio(self):
        """Тест 1.3. Обновление портфеля"""
        driver = self.driver
        self.login()
        delay = 5

        btn_to_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/header/nav/div/div/div[2]/div[1]/a[1]")))
        btn_to_portfolio.click()

        btn_update_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div[2]/main/div/div[3]/div/div[3]/div[1]/button[2]")))
        btn_update_portfolio.click()

        random_name = f"portfolio {randrange(99)}"
        input_name = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div[1]/input")
        input_name.send_keys(random_name)
        input_months = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div[2]/input")
        input_months.send_keys(10)
        btn_add = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
        btn_add.click()

        assert random_name in driver.page_source


    def test_analyze_portfolio(self):
        """Тест 1.7. Анализ портфеля"""
        driver = self.driver
        self.login()
        delay = 5

        btn_to_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/header/nav/div/div/div[2]/div[1]/a[1]")))
        btn_to_portfolio.click()

        btn_check_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/main/div/div[2]/div/div[3]/div[1]/div")))
        btn_check_portfolio.click()

        time.sleep(5)

        assert "Анализ на основе математической модели:" in driver.page_source


    def login(self):
        driver = self.driver
        driver.get(BASE_URL + "/login")
        email_input = driver.find_element(By.ID, "formBasicEmail")
        pass_input = driver.find_element(By.ID, "formBasicPassword")
        email_input.send_keys(AUTH_EMAIL)
        pass_input.send_keys(AUTH_PASS)
        btn_login = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[3]/button")
        btn_login.click()
        time.sleep(2)


    def test_adding_bond_to_portfolio(self):
        """Тест 2.1. Добавление в портфель облигаций"""
        driver = self.driver
        delay = 3
        self.login()
        btn_to_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/header/nav/div/div/div[2]/div[1]/a[1]")))
        btn_to_portfolio.click()
        btn_check_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/main/div/div[2]/div/div[3]/div[1]/div")))
        btn_check_portfolio.click()



        btn_to_bonds = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/header/nav/div/div/div[2]/div[1]/a[3]")))
        btn_to_bonds.click()

        btn_add_bonds = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/main/div/div[1]/div/div[3]")))
        btn_add_bonds.click()

        input_count = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div[1]/input")
        input_count.send_keys(3)
        portfolio = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div[2]/select")
        portfolio.send_keys("На жизнь - 100 лет")
        btn_add = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
        btn_add.click()

        btn_to_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/header/nav/div/div/div[2]/div[1]/a[1]")))
        btn_to_portfolio.click()
        btn_check_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/main/div/div[2]/div/div[3]/div[1]/div")))
        btn_check_portfolio.click()
        time.sleep(2)
        bond_info = driver.find_element(By.XPATH, "/html/body/div/div[2]/main/div/div[8]/div/div/div[2]")
        assert bond_info.text.split(' ')[0] in driver.page_source



    def test_adding_stock_to_portfolio(self):
        """Тест 3.1. Добавление в портфель акций"""
        delay = 5
        driver = self.driver
        self.login()
        btn_to_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/header/nav/div/div/div[2]/div[1]/a[1]")))
        btn_to_portfolio.click()
        btn_check_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/main/div/div[2]/div/div[3]/div[1]/div")))
        btn_check_portfolio.click()
        stock_info = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/main/div/div[6]/div/div/div[2]")))
        stock_count = int(stock_info.text.split(' ')[0])
        btn_to_stocks = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/header/nav/div/div/div[2]/div[1]/a[2]")))
        btn_to_stocks.click()
        btn_add_stock = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/main/div/div[1]/div/div[3]")))
        btn_add_stock.click()
        input_count = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div[1]/input")
        input_count.send_keys(3)
        portfolio = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div[2]/select")
        portfolio.send_keys("На жизнь - 100 лет")
        btn_add = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
        btn_add.click()
        time.sleep(2)
        btn_to_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/header/nav/div/div/div[2]/div[1]/a[1]")))
        btn_to_portfolio.click()
        btn_check_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/main/div/div[2]/div/div[3]/div[1]/div")))
        btn_check_portfolio.click()
        time.sleep(2)
        stock_info = driver.find_element(By.XPATH, "/html/body/div/div[2]/main/div/div[6]/div/div/div[2]")
        assert int(stock_info.text.split(' ')[0]) == 3 + stock_count


    def test_login(self):
        """Тест 4.1. Регистрация пользователя"""
        driver = self.driver
        driver.get(BASE_URL + "/login")
        email_input = driver.find_element(By.ID, "formBasicEmail")
        pass_input = driver.find_element(By.ID, "formBasicPassword")
        email_input.send_keys(AUTH_EMAIL)
        pass_input.send_keys(AUTH_PASS)
        btn_login = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/form/div[3]/button')))
        btn_login.click()
        time.sleep(2)
        assert "Информация на данном сайте представлена" in driver.page_source

    def test_navigation_to_portfolio(self):
        """Тестирование навигации (модуль портфели)"""
        driver = self.driver
        self.login()
        delay = 3
        btn_to_portfolio = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/header/nav/div/div/div[2]/div[1]/a[1]')))
        btn_to_portfolio.click()
        time.sleep(2)
        assert "Подробнее" in driver.page_source

    def test_navigation_to_stocks(self):
        """Тестирование навигации (модуль акции)"""
        driver = self.driver
        self.login()
        btn_to_stocks = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/header/nav/div/div/div[2]/div[1]/a[2]')))
        btn_to_stocks.click()
        time.sleep(1)
        assert "Добавить в портфель" in driver.page_source

def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
