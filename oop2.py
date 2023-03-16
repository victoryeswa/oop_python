class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self, students):
        if len(self.students) < self.max_students:
            self.students.append(students)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value/len(self.students)

s1 = Student('Tim', 19, 95)
s2 = Student('Bill', 19, 75)
s3 = Student('Jill', 19, 65)

course = Course('Science', 2)
course.add_students(s1)
course.add_students(s2)
print(course.students[0].name)
print(course.get_average_grade())

#finished up on the basics 