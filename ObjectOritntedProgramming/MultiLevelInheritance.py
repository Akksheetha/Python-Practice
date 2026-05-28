class student:
    def getStudentInfo(self):
        self.__rollno=input("Enter Roll Number:")
        self.__name=input("Enter Name:")
    def printStudentInfo(self):
        print("Roll Number:",self.__rollno,"Name:",self.__name)
class Marks(student):
    def getmarks(self):
        self.getStudentInfo()
        self.__marks1=float(input("Enter marks for subject 1:"))
        self.__marks2=float(input("Enter marks for subject 2:"))
        self.__marks3=float(input("Enter marks for subject 3:"))
    def printmarks(self):
        self.printStudentInfo()
        print("MArks1:",self.__marks1)
        print("MArks2:",self.__marks2)
        print("MArks3:",self.__marks3)

    def calcTotalMarks(self):
        return self.__marks1+self.__marks2+self.__marks3
    
m = Marks()
m.getmarks()
m.printmarks()
print("Total Marks:", m.calcTotalMarks())
