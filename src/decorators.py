import functools
import logging

def log(filename=None):
    # Настройка логирования
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Логируем начало выполнения функции
            logging.info(f'Starting function: {func.__name__} with arguments: {args}, {kwargs}')
            try:
                result = func(*args, **kwargs)
                # Логируем результат выполнения
                logging.info(f'Function: {func.__name__} completed successfully with result: {result}')
                return result
            except Exception as e:
                # Логируем ошибку
                logging.error(f'Function: {func.__name__} raised {type(e).__name__} with arguments: {args}, {kwargs}')
                raise  # Повторно поднимаем исключение
        return wrapper
    return decorator