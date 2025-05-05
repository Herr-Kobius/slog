import typing

from slog.logger import Logger, logging

__all__ = ['log_function_call', 'log_function_call_with_time'] 

logs_folder = './logs'

global_logger = Logger('All', logs_folder, console_level=logging.INFO)
print(f'Log File Time Stemp:{global_logger.file_name}')

def log_function_call(func: typing.Callable) -> typing.Callable:
    def wrap(*args, **kwargs):
        global_logger.info(f"Called {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrap

def log_function_call_with_time(func: typing.Callable) -> typing.Callable:
    import time
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        global_logger.info(f"Called {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        end = time.time()
        global_logger.info(f'Function {func.__name__} executed in {(end-start):.5f}s')
        return result
    return wrapper

del typing