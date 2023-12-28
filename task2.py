# task2.py
from data_service import generate_student_list

def print_student_info(student):
    print(f"Name: {student.first_name} {student.last_name}")
    print(f"Birth Date: {student.birth_date}")
    print("Subjects:")
    for subject in student.subjects:
        print(f"- {subject['subject']}, Exam Date: {subject['exam_date']}, Teacher: {subject['teacher']}")
    print("\n")

def print_exam_dates_table(students):
    print("Exam Dates Table:")
    print("{:<20} {:<20} {:<20} {:<20}".format("First Name", "Last Name", "Subject", "Exam Date"))
    for student in students:
        first_row = True
        for subject in student.subjects:
            exam_date_str = subject['exam_date'].strftime('%Y-%m-%d')
            first_name = student.first_name if first_row else ''
            last_name = student.last_name if first_row else ''
            print("{:<20} {:<20} {:<20} {:<20}".format(first_name, last_name,
                                                          subject['subject'], exam_date_str))
            first_row = False

def main():
    students = generate_student_list()

    print("Student List:")
    for student in students:
        print_student_info(student)

    print_exam_dates_table(students)

if __name__ == "__main__":
    main()

