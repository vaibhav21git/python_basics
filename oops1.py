# in oops two types of variable
# 1)instance variable
# 2)class variable

# if you define a variable inside a init function then it is a instance variable
# but if outside the init it is class variable;
# namespace is an area where you create and store object/variable


class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 8

Car.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil)
