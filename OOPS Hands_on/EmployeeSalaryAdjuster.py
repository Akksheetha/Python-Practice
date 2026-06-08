class Employee:
    def getInfo(self, salary, hours):
        self.salary = salary
        self.hours = hours
    def AddSal(self):
        if self.salary < 500:
            self.salary += 10
    def AddWork(self):
        if self.hours > 6:
            self.salary += 5
emp = Employee()
emp.getInfo(450, 8)
emp.AddSal()
emp.AddWork()
print("Final Salary:", emp.salary)