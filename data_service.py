# data_service.py
from datetime import date, timedelta

class Student:
    def __init__(self, first_name, last_name, birth_date, subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.subjects = subjects

def generate_student_list():
    students_data = [
        {"first_name": "Иван", "last_name": "Иванов", "birth_date": date(2002, 2, 3),
         "subjects": [
             {"subject": "Линейная алгебра", "exam_date": date(2023, 12, 27), "teacher": "Прискин Олег Юрьевич"},
             {"subject": "Программирование", "exam_date": date(2023, 12, 24), "teacher": "Надеждин Максим Александрович"},
             {"subject": "Базы данных", "exam_date": date(2024, 1, 10), "teacher": "Финская Марина Юрьевна"}
         ]},
        {"first_name": "Макс", "last_name": "Кудин", "birth_date": date(2002, 9, 27),
         "subjects": [
             {"subject": "Логика", "exam_date": date(2023, 12, 26), "teacher": "Кутлин Александр Григорьевич"},
             {"subject": "Программирование", "exam_date": date(2023, 12, 24), "teacher": "Надеждин Максим Александрович"},
             {"subject": "Базы данных", "exam_date": date(2024, 1, 10), "teacher": "Финская Марина Юрьевна"},
             {"subject": "Линейная алгебра", "exam_date": date(2023, 12, 27), "teacher": "Прискин Олег Юрьевич"}
         ]},
        {"first_name": "Андрей", "last_name": "Верхов", "birth_date": date(2002, 6, 16),
         "subjects": [
             {"subject": "Линейная алгебра", "exam_date": date(2023, 12, 27), "teacher": "Прискин Олег Юрьевич"},
             {"subject": "Пентест", "exam_date": date(2024, 1, 14), "teacher": "Худрич Юрий Александрович"},
             {"subject": "Базы данных", "exam_date": date(2024, 1, 10), "teacher": "Финская Марина Юрьевна"}
         ]},
        {"first_name": "Геннадий", "last_name": "Бирюков", "birth_date": date(2003, 4, 9),
         "subjects": [
             {"subject": "Линейная алгебра", "exam_date": date(2023, 12, 27), "teacher": "Прискин Олег Юрьевич"},
             {"subject": "Пентест", "exam_date": date(2024, 1, 14), "teacher": "Худрич Юрий Александрович"},
             {"subject": "Английский язык", "exam_date": date(2024, 1, 15), "teacher": "Пиреева Арина Сергеевна"},
             {"subject": "Базы данных", "exam_date": date(2024, 1, 10), "teacher": "Финская Марина Юрьевна"}
         ]},
        {"first_name": "Григорий", "last_name": "Авдеев", "birth_date": date(2001, 12, 29),
         "subjects": [
             {"subject": "Линейная алгебра", "exam_date": date(2023, 12, 27), "teacher": "Прискин Олег Юрьевич"},
             {"subject": "Пентест", "exam_date": date(2024, 1, 14), "teacher": "Худрич Юрий Александрович"},
             {"subject": "Английский язык", "exam_date": date(2024, 1, 15), "teacher": "Пиреева Арина Сергеевна"},
             {"subject": "Программирование", "exam_date": date(2023, 12, 24), "teacher": "Надеждин Максим Александрович"}
         ]}
    ]

    students = []
    for student_data in students_data:
        student = Student(
            first_name=student_data["first_name"],
            last_name=student_data["last_name"],
            birth_date=student_data["birth_date"],
            subjects=student_data["subjects"]
        )
        students.append(student)
    return students

