import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

from bot.services.constants import PARSING_URL

load_dotenv()

DEV_MODE = os.getenv("DEV_MODE")
print(DEV_MODE)


class FgisParser:

    def __driver_settings() -> WebDriver:
        chrome_options_ = Options()
        chrome_options_.add_argument('--verbose')
        chrome_options_.add_argument('--headless')
        chrome_options_.binary_location = '/usr/bin/google-chrome'
        if not DEV_MODE:
            chrome_options_.binary_location = '/usr/bin/chromium-browser'
        chrome_options_.binary_location = '/usr/bin/google-chrome'
        chrome_options_.add_argument('--no-sandbox')
        chrome_options_.add_argument('--disable-dev-shm-usage')
        driver_ = webdriver.Chrome(options=chrome_options_)
        return driver_

    def get_calibration_info(
            self, suitability: bool = True, sensor_type: str = '', sensor_number: str = ''
    ) -> list[list[str]]:
        if sensor_type is None:
            sensor_type = ''
        if sensor_number is None:
            sensor_number = ''

        driver: webdriver.Chrome = self.__driver_settings()
        url = PARSING_URL.format(suitability, sensor_type, sensor_number)
        driver.get(url)

        wait = WebDriverWait(driver, 20)

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary"]'))).click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//tbody/tr')))

            table_rows = driver.find_elements(By.XPATH, '//tbody/tr')

            calibration_dates = [
                ['Дата поверки', 'Организация', 'Тип СИ', 'Заводской номер']
            ]
            for row in table_rows:
                organization_element = row.find_element(By.XPATH, './td[1]')
                ci_element = row.find_element(By.XPATH, './td[4]')
                ci_number = row.find_element(By.XPATH, './td[6]')
                calibration_date_element = row.find_element(By.XPATH, './td[7]')
                calibration_dates.append(
                    [
                        calibration_date_element.text,
                        organization_element.text,
                        ci_element.text,
                        ci_number.text
                    ]
                )

            return calibration_dates
        except BaseException as e:
            return (f'Информация о поверке не найдена. Ошибка: {e}')
        finally:
            driver.quit()
