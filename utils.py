from slog.logger import Logger, logging

logs_folder = './logs'

global_logger = Logger('All', logs_folder, console_level=logging.DEBUG)
print(f'Log File Time Stemp:{global_logger.file_name}')

def log_function_call(func):
    def wrap(*args, **kwargs):
        global_logger.info(f"Called {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrap