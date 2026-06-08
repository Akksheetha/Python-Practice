class Student:
    def __init__(self, student_id=0, name="Unknown", age=0, grade="Unknown"):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
s1 = Student()
s2 = Student(101, "John Doe", 15, "10th")
print(s1.name, s2.name)