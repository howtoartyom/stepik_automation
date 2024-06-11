import argparse
from selenium import webdriver
import time
from logger_config import configure_logger
from auth import login_to_stepik
from navigation import navigate_steps

# Настройка логирования
logger = configure_logger()

# Настройка аргументов командной строки
parser = argparse.ArgumentParser(description="Automation script for Stepik lessons")
parser.add_argument("lesson_url", type=str, help="URL of the lesson")
parser.add_argument("login", type=str, help="Email for Stepik login")
parser.add_argument("password", type=str, help="Password for Stepik login")
parser.add_argument("--action", choices=["download", "import"], required=True, help="Action to perform on steps: download or import")

args = parser.parse_args()

# Инициализация ChromeDriver
driver = webdriver.Chrome()
driver.get(args.lesson_url)
time.sleep(5)

try:
    # Авторизация
    login_to_stepik(driver, args.login, args.password, logger)

    # Задержка для завершения авторизации
    time.sleep(5)

    # Получаем идентификатор урока из URL текущего шага после нажатия Edit
    initial_step_url = driver.current_url
    lesson_id = initial_step_url.split('/')[4]

    # Навигация по шагам урока
    navigate_steps(driver, lesson_id, initial_step_url, logger, args.action)

except Exception as e:
    logger.error(f"Появилась ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()
