import logging
import time
import os
from slog.color_formatter import ColorFormatter

class Logger(logging.Logger):
    def __init__(self, name: str, path:str, console_level:int=logging.WARNING, file_level:int=logging.DEBUG, file_suffix:str='') -> None:
        super().__init__(name, logging.DEBUG)

        sh_formatter = ColorFormatter('%(asctime)s.%(msecs)03d [%(name)s] %(levelname)s %(message)s', '%H:%M:%S')
        fh_formatter = logging.Formatter('%(asctime)s.%(msecs)03d [%(name)s] %(levelname)s %(message)s', '%m-%d %H:%M:%S')

        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        console_handler.setFormatter(sh_formatter)

        self.path = path
        self.file_name = str(int(round(time.time(), 0)))[-8:] + file_suffix + '.log'

        file_handler = logging.FileHandler(f'{path}/{self.file_name}')
        file_handler.setLevel(file_level)
        file_handler.setFormatter(fh_formatter)

        self.addHandler(console_handler)
        self.addHandler(file_handler)

    def set_console_level(self, console_level:int):
        self.handlers[0].setLevel(console_level)

    def set_file_level(self, file_level:int):
        self.handlers[1].setLevel(file_level)

    def remove_logs(self, path:str|None=None, keep:int=1) -> None:
        path = self.path if path==None else path
        log_files = sorted(os.listdir(path))
        for _, file_name in zip(range(len(log_files)-keep), log_files):
            if file_name.endswith('.log'):
                os.remove(os.path.join(path, file_name))

