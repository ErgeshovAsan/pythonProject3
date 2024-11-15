class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self, full_name, age, is_married):
        print(f'full_name: {self.full_name}, age: {self.age}, is_married: {self.is_married}')


class Student(Person):
    def __init__(self, full_name, age, is_married, marks=None):
        super().__init__(full_name, age, is_married)
        self.marks = marks if marks is not None else {}

    def average_rating(self):
        return print(f'average rating: {sum(self.marks.values()) / len(self.marks)}')


class Teacher(Person):
    base_salary = 50000

    def __init__(self, full_name, age, is_married, experience=0):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def salary_bonus(self):
        if self.experience > 3:
            while self.experience - 3 > 0:
                Teacher.base_salary += Teacher.base_salary * 0.05
                self.experience -= 1
            print(f'salary bonus: {Teacher.base_salary}')
        else:
            print(f'base salary: {Teacher.base_salary}')


teacher = Teacher('Sasha', 21, 'False', 5)
print(
    f'full name: {teacher.full_name}, age: {teacher.age}, is married: {teacher.is_married}, experience: {teacher.experience}')
teacher.salary_bonus()


def create_students():
    student1 = Student("Alice", 19, True, {"Math": 4, "English": 5, "Science": 3})
    student2 = Student("Bob", 17, False, {"Math": 5, "English": 5, "Science": 5})
    student3 = Student("Clara", 18, False, {"Math": 3, "English": 3, "Science": 3})

    students = [student1, student2, student3]
    return students


students = create_students()
for student in students:
    print(
        f'full name: {student.full_name}, age: {student.age}, is married: {student.is_married}, marks: {student.marks}')
    student.average_rating()
