import logging
import os

# Создаем папку logs, если она не существует
os.makedirs("logs", exist_ok=True)

# Настраиваем формат логирования
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

# Настраиваем логирование для masks
masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)
masks_handler = logging.FileHandler("logs/masks.log", mode="w")
masks_handler.setFormatter(logging.Formatter(log_format, datefmt=date_format))
masks_logger.addHandler(masks_handler)

# Настраиваем логирование для utils
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)
utils_handler = logging.FileHandler("logs/utils.log", mode="w")
utils_handler.setFormatter(logging.Formatter(log_format, datefmt=date_format))
utils_logger.addHandler(utils_handler)
