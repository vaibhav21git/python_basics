# INHERITANCE
# super class A
# sub class B
# constructor will call a method which is init
# constructor of B will also call the constructor of A
# from top to bottom priority if two different parent class at same level
# to represent super class we use super method


class A:
    def feature1(self):
        print("feature 1A working")

    def feature2(self):
        print("feature 2A working")

    def __init__(self):
        print("In A Init")


class B:
    def feature1(self):
        print("feature 1B working")

    def feature2(self):
        print("feature 2B working")

    # def __init__(self):
    #     super().__init__()
    #     print("in B init")


class C(A, B):
    def __init__(self):
        print("in c init")

    def feat(self):
        super().feature2()


c1 = C()
c1.feature1()
c1.feat()
