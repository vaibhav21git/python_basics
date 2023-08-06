# all the objects are present in the heap memory
# class cannot be empty instead u should write pass
# q1) who allocates the size of object
# a1) it is the constructor who allocates the size of object
# self is like a pointer  it will point based on c1.update() where c1 is
# passed as an argument in update function


class Computer:
    def __init__(self):
        self.name = "vaibhav"
        self.age = 23

    def update(self):
        self.age = 87

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c1.age = 24
c2 = Computer()

# c1 is comparing itself with c2
if c1.compare(c2):
    print("they are same")
else:
    print("they are different")


print(c1.name)
