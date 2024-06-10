import logging


def configure_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Создание обработчика для записи логов в файл
    file_handler = logging.FileHandler('lesson_script.log')
    file_handler.setLevel(logging.INFO)

    # Создание обработчика для вывода логов в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Настройка формата логов
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Добавление обработчиков в логгер
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
