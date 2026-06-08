class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
    def displayInfo(self):
        print(f"ID: {self.emp_id}, Name: {self.name}")
    def calculateSalary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary
    def calculateSalary(self):
        return self.monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculateSalary(self):
        return self.hourly_rate * self.hours_worked
class ContractEmployee(Employee):
    def __init__(self, emp_id, name, duration, fixed_rate):
        super().__init__(emp_id, name)
        self.duration = duration
        self.fixed_rate = fixed_rate
    def calculateSalary(self):
        return self.duration * self.fixed_rate
ft = FullTimeEmployee(1, "Alice", 3000)
pt = PartTimeEmployee(2, "Bob", 20, 80)
ft.displayInfo()
print("FullTime Salary:", ft.calculateSalary())
pt.displayInfo()
print("PartTime Salary:", pt.calculateSalary())