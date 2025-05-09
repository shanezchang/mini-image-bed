import logging
import re
from logging.handlers import TimedRotatingFileHandler

from core.constant import LOG_PATH_DEFAULT


def logger(
        log_path: str = None,
        log_console: bool = True,
        log_keep_days: int = 30,
) -> logging.Logger:
    if not log_path:
        log_path = LOG_PATH_DEFAULT
    log_handle = logging.getLogger(log_path)

    formatter = logging.Formatter(
        "%(process)d - %(thread)d - %(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s"
    )

    log_handle.setLevel(logging.INFO)

    if log_console:
        log_screen = logging.StreamHandler()
        log_screen.setFormatter(formatter)
        log_handle.addHandler(log_screen)
        pass

    file_handler = TimedRotatingFileHandler(
        filename=log_path,
        when="MIDNIGHT",
        interval=1,
        backupCount=log_keep_days,
    )
    file_handler.suffix = "%Y-%m-%d.log"
    file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
    file_handler.setFormatter(formatter)
    log_handle.addHandler(file_handler)
    return log_handle


log = logger()
