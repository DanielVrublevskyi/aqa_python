import logging
# create common format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# set up cli_logger with own Level, as StreamHandler, with common format
cli_logger = logging.getLogger("cli_logger")
cli_logger.setLevel(logging.DEBUG)
cli_logger.propagate = False

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

cli_logger.addHandler(console_handler)

# set up file_logger with own Level, as FileHandler in spec file, with common format
file_logger = logging.getLogger("file_logger")
file_logger.setLevel(logging.DEBUG)
file_logger.propagate = False

file_handler = logging.FileHandler("login_system.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

file_logger.addHandler(file_handler)