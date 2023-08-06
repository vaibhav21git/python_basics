# Polymorphism - One thing can take many forms


# DUCK TYPING IN PYTHON

# IF BEHAVIOR OF A BIRD IS LIKE A DUCK THEN THE BIRD IS A DUCK

# the moment you give a name to variable that just the name of memeory assigned
# to that variable


class Pycharm:
    def execute(self):
        print("compiling")
        print("running")


class MyEditor:
    def execute(self):
        print("spell check")
        print("convention check")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = Pycharm()


lap1 = Laptop()

lap1.code(ide)
