from datetime import datetime

from core.utils.logger import get_file_logger

file_logger = get_file_logger("hb_test.log")

key = "TSTFEED0300|7E3E|0400"
def get_time_dt(full_str):
    format_string = '%H:%M:%S'
    time_str_len = 8
    start = full_str.find("Timestamp ") + len("Timestamp ")
    time_str = full_str[start : (start + time_str_len)]

    return datetime.strptime(time_str, format_string)



with open("hblog.txt", "r") as file:
    previous_time = None

    for line in file:
        if key in line:
            current_time = get_time_dt(line)

            if previous_time is not None:
                difference = previous_time - current_time
                if difference.total_seconds() >= 33:
                    file_logger.error(f"{current_time.strftime("%H:%M:%S")} - difference: {str(difference)}")
                elif 31 < difference.total_seconds() < 33:
                    file_logger.warning(f"{current_time.strftime("%H:%M:%S")} - difference: {str(difference)}")

            previous_time = current_time