import requests
import logging
from core.utils.logger import cli_logger

class RequestUtils:
    def __init__(self, log_file=None):
        self.file_logger = None

        if log_file:
            self.set_file_logger(log_file)

    def set_file_logger(self, file_name):
        logger = logging.getLogger(f'{file_name}_logger')
        logger.setLevel(logging.INFO)
        logger.propagate = False

        if not logger.handlers:
            handler = logging.FileHandler(f'{file_name}.log')
            handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            logger.addHandler(handler)

        self.file_logger = logger


    def send_request(self, method, path, params=None,
                     json=None, headers=None, exp_status_code=None, *args, **kwargs):

        if method.upper() == 'GET':
            response = requests.get(path, params=params, headers=headers)

        elif method.upper() == 'POST':
            response = requests.post(path, json=json, headers=headers, **kwargs)

        elif method.upper() == 'PUT':
            response = requests.put(path, json=json, headers=headers)

        elif method.upper() == 'DELETE':
            response = requests.delete(path, params=params, json=json, headers=headers)

        else:
            raise AttributeError(f'Method {method} not supported')

        message = f"{response.request.method}: {response.request.url}"
        cli_logger.info(message)
        if self.file_logger is not None:
            self.file_logger.info(message)

        if exp_status_code is not None:
            assert response.status_code == exp_status_code, f'Status code should be {exp_status_code}'
        return response