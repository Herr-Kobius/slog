import logging
import colorama

from typing import Any
from collections.abc import Mapping


class ColorFormatter(logging.Formatter):
    def __init__(self, fmt: str | None = None, datefmt: str | None = None, style  = "%", validate: bool = True, *, defaults: Mapping[str, Any] | None = None) -> None:
        super().__init__(fmt, datefmt, style, validate, defaults=defaults)

    def format(self, record: logging.LogRecord) -> str:
        log =  super().format(record)
        log = log.replace('DEBUG', colorama.Fore.BLUE+'DEBUG'+colorama.Fore.RESET)
        log = log.replace('INFO', colorama.Fore.WHITE+'INFO'+colorama.Fore.RESET)
        log = log.replace('WARNING', colorama.Fore.YELLOW+'WARNING'+colorama.Fore.RESET)
        log = log.replace('ERROR', colorama.Fore.RED+'WARNING'+colorama.Fore.RESET)
        log = log.replace('CRITICAL', colorama.Fore.RED+'CRITICAL'+colorama.Fore.RESET)
        
        return log
