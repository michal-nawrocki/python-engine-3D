import logging
from typing import Union


def _super_format():
    return logging.Formatter('%(levelname)s %(asctime)s [%(module)s.%(funcName)s:%(lineno)s] %(message)s')


def _default_format():
    return logging.Formatter(
        "%(levelname)s %(asctime)s.%(msecs)03d {%(threadName)s} {%(module)s.%(funcName)-18s:%(lineno)s} %(message)s",
        "%H:%M:%S"
    )


def get_a_logger(name: str, level: Union[int, str] = 'DEBUG', format_type: str = " ") -> logging.Logger:
    stream_handler = logging.StreamHandler()

    logger_format = _default_format() if format_type is " " else _super_format()

    stream_handler.setFormatter(logger_format)
    stream_handler.setLevel(logging.getLevelName(level))

    logger = logging.getLogger(name)

    logger.setLevel(logging.getLevelName(level))
    logger.addHandler(stream_handler)

    return logger
