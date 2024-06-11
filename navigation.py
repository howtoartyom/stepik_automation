from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def navigate_steps(driver, lesson_id, initial_step_url, logger, action):
    step_number = 1

    while True:
        try:
            # Переход к текущему шагу
            current_step_url = f"https://stepik.org/edit-lesson/{lesson_id}/step/{step_number}"
            driver.get(current_step_url)
            logger.info(f"Перешли к шагу: {current_step_url}")
            time.sleep(5)

            # Поиск элементов с заголовками "Code Challenge" или "Программирование"
            test_cases = driver.find_elements(By.XPATH,
                                              "//div[@class='step-editor__header']/h2[contains(., 'Code Challenge') or contains(., 'Программирование')]")

            if test_cases:
                logger.info("Шаг содержит код")

                # Нажатие на кнопку меню
                menu_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[@class='st-button_style_none step-editor__menu-toggler']"))
                )
                menu_button.click()
                logger.info("Нажато на ...")

                # Нажатие на кнопку скачивания или импорта в зависимости от действия
                if action == "download":
                    action_button = WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH,
                                                    "//a[contains(@class, 'download-step') and (contains(text(), 'Download step') or contains(text(), 'Скачать шаг'))]"))
                    )
                    action_button.click()
                    logger.info("Нажали на кнопку скачивания шага")
                elif action == "import":
                    action_button = WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH,
                                                    "/html/body/main/div/div[1]/article/section/div[1]/div/div[2]/div/div/ul/li[3]/button"))
                    )
                    action_button.click()
                    logger.info("Нажали на кнопку импорта шага")
                    time.sleep(10)

                    # Нажатие на кнопку "Сохранить"
                    save_button = WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH,
                                                    "/html/body/main/div/div[2]/div/div[2]/button[1]"))
                    )
                    save_button.click()
                    logger.info("Нажали на кнопку сохранения шага")

                time.sleep(5)
                logger.info(f"Шаг {action} выполнен")
            else:
                logger.info("Шаг не содержит код")

            # Проверка окончания урока
            current_url = driver.current_url
            if current_url == initial_step_url or lesson_id not in current_url:
                logger.info("Урок закончен")
                break

            if f"/step/{step_number}" not in current_url and current_url != initial_step_url:
                logger.info("Урок закончен")
                break

            # Переход к следующему шагу
            step_number += 1

        except TimeoutException:
            logger.info("Следующий шаг не найден, урок закончен")
            break
