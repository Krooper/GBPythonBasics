"""
2)Нужно написать программу
В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
В самой программе вводим список всех студентов.
В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых низкие оценки
"""


def fill_students():
    stud_number = input('Введите кол-во студентов: ')
    students_lst = []
    for i in range(0, int(stud_number)):
        students_lst.append(Student(input('Введите имя студента: '), input('Введите номер группы: ')))
    return students_lst


def fill_stud_progress(students_lst):
    for student in students_lst:
        student.fill_progress()
    return students_lst


def stud_sort_key(student):
    return student.name[0]


def low_marks(students_lst):
    low_marks_lst = []
    for student in students_lst:
        for subject, mark in student.progress.items():
            if int(mark) <= 3:
                low_marks_lst.append(student)
                break
    return low_marks_lst


class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.progress = dict()

    def fill_progress(self):
        subject_lst = ['Русский язык', 'Математика', 'Физика', 'Литература', 'Физ-ра']
        self.progress = {}
        print(f'Успеваемость студента - {self.name}: ')
        for subject in subject_lst:
            self.progress[subject] = input(f'Введите оценку по предмету {subject}: ')
        return self.progress

    def __str__(self):
        progress_str = ''
        for subject, mark in self.progress.items():
            progress_str += f'{subject} - {mark}\n'
        return f'Студент - {self.name}\nНомер группы - {self.group}\nУспеваемость:\n{progress_str}'


class Journal:
    def __init__(self, students):
        self.students = students

    def sort_students(self, sort_key):
        return self.students.sort(key=sort_key)

    def __str__(self):
        self.sort_students(stud_sort_key)
        print("Список студентов по алфавиту: ")
        out_str = ''
        for student in self.students:
            out_str += f'{str(student)}\n'
        return out_str


NewJournal = Journal(fill_stud_progress(fill_students()))
print()
print(NewJournal)

LowMarksJournal = Journal(low_marks(NewJournal.students))
print('Студенты с низкой успеваемостью:')
print(LowMarksJournal)
