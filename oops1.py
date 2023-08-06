# get the value of variables  - accesors
# modify the value of variables - mutators
# @classmethod are decorators
# static method is nothing to do with class variable and instance variable
# why none is printing in staticmethod doubt


class Student:
    school = "vaibhav university"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("this is student class in abc module")


s1 = Student(99, 76, 34)
s2 = Student(90, 55, 77)


print(Student.info())
