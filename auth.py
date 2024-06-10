from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_to_stepik(driver, login, password, logger):
    try:
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'navbar__auth_login') and text()='Войти']"))
        )
        login_button.click()
        logger.info("Вводим логин")

        email_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'id_login_email'))
        )
        email_field.send_keys(login)

        password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'id_login_password'))
        )
        password_field.send_keys(password)

        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'sign-form__btn') and @type='submit']"))
        )
        submit_button.click()
        logger.info("Входим в аккаунт")
    except Exception as e:
        logger.error(f"Не удалось войти: {e}")
        raise
