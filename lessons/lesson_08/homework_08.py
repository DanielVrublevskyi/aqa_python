#Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.
class Student:
    def __init__(self, name: str, last_name: str, age: int, score: float):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.score = score

    def set_score(self, new_score: float):
        self.score = new_score
        return self.score


student1 = Student("Alex", "Brown", 19, 87.5)
student2 = Student("Maria", "Wilson", 22, 94.2)
student3 = Student("John", "Miller", 18, 71.8)
print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)

student1.set_score(92.2)
print(student1.__dict__)