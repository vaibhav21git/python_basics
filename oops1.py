# method overriding
# due to inheritance
# my phone rides my fathers phone if i have a phone
# otherwise   my fathers phone is my phone


class A:
    def show(self):
        print("in A Show")


class B(A):
    pass


b1 = B()
b1.show()
