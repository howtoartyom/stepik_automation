from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_to_stepik(driver, login, password, logger):
    try:
        # Проверяем язык страницы
        if "Войти" in driver.page_source:
            login_button_text = 'Войти'
            email_field_id = 'id_login_email'
            password_field_id = 'id_login_password'
            submit_button_xpath = "//button[contains(@class, 'sign-form__btn') and @type='submit']"
        else:
            login_button_text = 'Log in'
            email_field_id = 'id_login_email'
            password_field_id = 'id_login_password'
            submit_button_xpath = "//button[contains(@class, 'sign-form__btn') and @type='submit']"

        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(@class, 'navbar__auth_login') and text()='{login_button_text}']"))
        )
        login_button.click()
        logger.info("Нажата кнопка входа")

        email_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, email_field_id))
        )
        email_field.send_keys(login)

        password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, password_field_id))
        )
        password_field.send_keys(password)

        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, submit_button_xpath))
        )
        submit_button.click()
        logger.info("Произведен вход в аккаунт")
    except Exception as e:
        logger.error(f"Не удалось войти: {e}")
        raise
