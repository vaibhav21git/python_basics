# integer float double are pre-built classes
# attributes are variables
# behavior are methods(functions)
# def __init__(self) is like a constructor
# init will be called automatically
# if u want the argument to be in part of object then u should
# use self.name = name


class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is", self.cpu, self.ram)


com1 = Computer("i5", 16)
com2 = Computer("Ryzen 5", 8)


com1.config()
com2.config()
