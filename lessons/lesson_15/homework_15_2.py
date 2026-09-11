from core.config import PROJECT_DIR
from core.utils.logger import file_logger
import json

test_dir = PROJECT_DIR / "lessons" / "lesson_15"
json_1 = test_dir / "localizations_en.json"
json_2 = test_dir / "localizations_ru.json"
json_3 = test_dir / "login.json"
json_4 = test_dir / "swagger.json"

files_list = [json_1, json_2, json_3, json_4]
for f in files_list:
    try:
        with f.open("r", encoding="utf-8") as file:
            data = json.load(file)

    except json.JSONDecodeError:
        file_logger.error(f"{f} is invalid json file")
