import logging
import time
import os
from slog.color_formatter import ColorFormatter

class Logger(logging.Logger):
    def __init__(self, name: str, path:str, console_level:int=logging.WARNING, file_level:int=logging.DEBUG, file_suffix:str='') -> None:
        super().__init__(name, logging.DEBUG)

        sh_formatter = ColorFormatter('%(asctime)s.%(msecs)03d [%(name)s] %(levelname)s %(message)s', '%H:%M:%S')
        fh_formatter = logging.Formatter('%(asctime)s.%(msecs)03d [%(name)s] %(levelname)s %(message)s', '%m-%d %H:%M:%S')

        sh = logging.StreamHandler()
        sh.setLevel(console_level)
        sh.setFormatter(sh_formatter)

        self.file_name = str(int(round(time.time(), 0)))[-7:] + file_suffix + '.log'

        fh = logging.FileHandler(f'{path}/{self.file_name}')
        fh.setLevel(file_level)
        fh.setFormatter(fh_formatter)

        self.addHandler(sh)
        self.addHandler(fh)
