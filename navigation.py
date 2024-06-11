from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def navigate_steps(driver, lesson_id, initial_step_url, logger):
    step_number = 1

    while True:
        try:
            test_cases = driver.find_elements(By.XPATH,
                                              "//div[@class='step-editor__header']/h2[contains(., 'Code Challenge') or contains(., 'Программирование')]")
            if test_cases:
                logger.info("Шаг содержит код")

                menu_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[@class='st-button_style_none step-editor__menu-toggler']")
                    )
                )
                menu_button.click()
                logger.info("Нажато на ...")

                download_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//a[contains(@class, 'download-step') and (contains(text(), 'Download step') or contains(text(), 'Скачать шаг'))]")
                    )
                )
                download_button.click()
                logger.info("Нажали на кнопку скачивания шага")
                time.sleep(5)
                logger.info("Шаг скачали")
            else:
                logger.info("Шаг не содержит код")

            step_number += 1
            next_step_url = f"https://stepik.org/edit-lesson/{lesson_id}/step/{step_number}"
            driver.get(next_step_url)
            logger.info(f"Перешли к следующему шагу: {next_step_url}")
            time.sleep(5)

            # Проверка, не достигли ли мы конца урока
            current_url = driver.current_url
            if current_url == initial_step_url or "step/new" in current_url or lesson_id not in current_url:
                logger.info("Урок закончен")
                break

        except TimeoutException:
            logger.info("Следующий шаг не найден, урок закончен")
            break
