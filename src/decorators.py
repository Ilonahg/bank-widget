import logging
import functools


def log(func=None, filename=None):
    """
    Декоратор для логирования вызовов функции.

    Параметры:
    func: функция, которую нужно декорировать.
    filename: необязательный параметр, если передан — логирование записывается в файл, иначе в консоль.
    """
    # Настроим логирование
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Если передан сам декоратор
    if func:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok: {result}")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
                raise  # Повторно выбрасываем исключение

        return wrapper

    # Если filename передан, но нет func, возвращаем только декоратор.
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok: {result}")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator if not func else decorator(func)
