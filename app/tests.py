import logging

# Loggerni sozlash
logger = logging.getLogger('custom_logger')

def log_message(level, message):
    """
    Berilgan level bo'yicha log yozadi.

    :param level: log darajasi (masalan, 'info', 'warning', 'error')
    :param message: log xabari
    """
    if level == 'info':
        logger.info(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'error':
        logger.error(message)
    elif level == 'debug':
        logger.debug(message)
    elif level == 'critical':
        logger.critical(message)
    else:
        logger.info("Log darajasi to'g'ri kiritilmagan. Standart 'info' darajasi ishlatiladi.")
        logger.info(message)
