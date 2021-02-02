class AppError(Exception):
    """
    Application Error base class
    """
    error_code = 1000
    log_msg = "Houston, we've got a problem"

    def __init__(self, message = None):
        if message is not None:
            self.log_msg = message

    def __str__(self):
        return (f'{self.error_code} - {self.log_msg}')


class JsonFormat(AppError):
    """
    Json format error derived class
    """
    error_code = 1001
    log_message = "Data is not JSON"


class DataError(AppError):
    """
    Data error derived class
    """
    error_code = 1002
    log_message = "URL did not return any data"
