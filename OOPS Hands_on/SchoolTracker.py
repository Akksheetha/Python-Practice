class School:
    totalStudents = 0
    MAX_CAPACITY = 500
    def enrollStudent(self):
        if School.totalStudents < School.MAX_CAPACITY:
            School.totalStudents += 1
        else:
            print("Capacity reached!")
    def getTotalStudents(self):
        return School.totalStudents
sch = School()
sch.enrollStudent()
sch.enrollStudent()
print("Total Students enrolled:", sch.getTotalStudents())