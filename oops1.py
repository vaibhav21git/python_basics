# integer float double are pre-built classes
# attributes are variables
# behavior are methods(functions)


class Computer:
    def config(self):
        print("i5, 16GB,1TB")


com1 = Computer()
com2 = Computer()
# this operation will give us the object of computer
# Computer.config is wrong
# you have to mention hey vaibhav walk, ravi walk not hey human walk

Computer.config(com1)
Computer.config(com2)

# below is generally used
com1.config()
