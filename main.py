from selenium import webdriver
import pyautogui
import time
from logger_config import configure_logger
from auth import login_to_stepik
from navigation import navigate_steps

# Настройка логирования
logger = configure_logger()

# Запрос данных у пользователя
lesson_url = pyautogui.prompt("Введите URL урока:")
login = pyautogui.prompt("Введите email:")
password = pyautogui.password("Введите пароль:")

# Инициализация EdgeDriver
driver = webdriver.Edge()
driver.get(lesson_url)

try:
    # Авторизация
    login_to_stepik(driver, login, password, logger)

    # Задержка для завершения авторизации
    time.sleep(5)

    # Получаем идентификатор урока из URL текущего шага после нажатия Edit
    initial_step_url = driver.current_url
    lesson_id = initial_step_url.split('/')[4]

    # Навигация по шагам урока
    navigate_steps(driver, lesson_id, initial_step_url, logger)

except Exception as e:
    logger.error(f"Появилась ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()
