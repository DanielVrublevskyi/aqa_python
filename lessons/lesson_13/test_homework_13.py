import pytest

from lessons.lesson_13 import homework_13
from core.utils.logger import cli_logger


@pytest.mark.parametrize(
    'name, sts',
    [
        ('Alex', 'success'),
        ('Max', 'expired'),
        ('Marti', 'other')
    ]
)
def test_logging_to_file(name, sts, request):
    homework_13.log_event(username = name, status = sts)
    cli_logger.info(f"Starting {request.node.name} test")

    filename = 'login_system.log'
    exp_row_value = f"Login event - Username: {name}, Status: {sts}"
    with open(filename) as f:
        last_row = f.readlines()[-1]

    assert last_row.__contains__(exp_row_value), f"The last log message should have Username: {name}, Status: {sts}"
    cli_logger.info(f"Finished {request.node.name} test")
