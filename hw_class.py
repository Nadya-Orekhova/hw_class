class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['Введение в программирование']
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_hw(self):
        count = 0
        for grades_key in self.grades:
            count += len(self.grades[grades_key])
        self.average_hw = round((sum(map(sum, self.grades.values())) / count), 2)
        return self.average_hw

    def __str__(self):
        return f"Имя:{ self.name}\n"f"Фамилия:{ self.surname }\n"f"Средняя оценка за домашние задания:\
{self.average_hw } \n"f"Курсы в процессе изучения: {','.join(self.courses_in_progress)}\n" f"Завершенные курсы:\
{','.join(self.finished_courses)}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет студента')
            return
        return self.average_hw() < other.average_hw()


    def count_mark(students, course):
      count = 0
      col = len(students)
      for student in students:
         if course not in student.grades:
            col -= 1
            continue
         else:
            count += (sum(student.grades[course]) / len(student.grades[course]))
      return round((count/col), 2)


    def add_courses(self,student_list) :
        self.name.append(student_list)


class Mentor:
     def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


    def average_lec(self):
        count = 0
        for grades_key in self.grades:
            count += len(self.grades[grades_key])
        self.average_lec = round((sum(map(sum, self.grades.values())) / count), 2)
        return self.average_lec

    def __str__(self):
        return f"Имя:{ self.name}\nФамилия:{self.surname} \n" f"Средняя оценка за лекции:{self.average_lec }"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет лектора')
            return
        return self.average_lec() < other.average_lec()


    def count_mark(lecturers, course):
      count = 0
      col = len(lecturers)
      for lecturer in lecturers:
         if course not in lecturer.grades:
            col -= 1
            continue
         else:
            count += (sum(lecturer.grades[course]) / len(lecturer.grades[course]))
      return round((count/col), 2)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя:{ self.name}\nФамилия:{self.surname}"


student_1 = Student('Ivan', 'Ivanov', 'male')
student_2 = Student('Daha', 'Vasileva', 'femal')
student_1.courses_in_progress += ['Python', 'Git']
student_2.courses_in_progress += ['Python', 'Git']

reviewer_1 = Reviewer('Some', 'Body')
reviewer_2 = Reviewer('Some', 'Body')
reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2.courses_attached += ['Python', 'Git']

lecturer_1 = Lecturer('Some', 'Body')
lecturer_2 = Lecturer('Some', 'Body')
lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2.courses_attached += ['Python', 'Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Git', 9)

reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Git', 9)

student_1.average_hw()
student_2.average_hw()

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
lecturer_1.average_lec()

print(reviewer_1)
print(lecturer_1)
print(student_1)
print(student_2)

