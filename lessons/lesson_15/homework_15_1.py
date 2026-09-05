import csv
from core.config import PROJECT_DIR

test_dir = PROJECT_DIR / "lessons" / "lesson_15"
random_csv_file = test_dir / "random.csv"
random_mich_csv_file = test_dir / "random-michaels.csv"

result_file_1 = test_dir / "result-random.csv"
result_file_2 = test_dir / "result-random-michaels.csv"

# убрать дубли из 1 файла
with random_csv_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    header_1 = reader.fieldnames
    rows_1 = list(reader)

unique_rows = []

for row in rows_1:
    if row not in unique_rows:
        unique_rows.append(row)


with result_file_1.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=header_1)

    writer.writeheader()
    writer.writerows(unique_rows)

# убрать дубли из 2 файла
with random_mich_csv_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    header_2 = reader.fieldnames
    rows_2 = list(reader)

unique_rows_2 = []

for row in rows_2:
    if row not in unique_rows_2:
        unique_rows_2.append(row)


with result_file_2.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=header_2)

    writer.writeheader()
    writer.writerows(unique_rows_2)

# сравнить хедеры

if set(header_1) != set(header_2):
    raise ValueError("CSV files have different headers")