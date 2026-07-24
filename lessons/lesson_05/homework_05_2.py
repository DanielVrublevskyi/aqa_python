# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# 1 - Add your new record o the beginning of the given list
tuple_to_begining = ('Sean', 'Brown', 35, 'Designer', 'Chicago')
people_records.insert(0, tuple_to_begining)
print(people_records[0])
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
people_records[1], people_records[5] = people_records[5], people_records[1]
print(people_records[1], people_records[5])
# 3 - check that all people in modified list with records indexes 6, 10, 13 have age >=30. Print condition check result
indexes = [6, 10, 13]
records_of_spec_indexes = []
for i in indexes:
    records_of_spec_indexes.append(people_records[i])

age_30 = False
for person in records_of_spec_indexes:
    if person[2] >= 30:
        age_30 = True
    else:
        age_30 = False
        break
print(age_30)
