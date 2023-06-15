class grandfather():
    def __init__(self, age):
        print("Age of the Grandfather: ",age)
    def intro(self):
        print("I am Grandfather of my grandson and father of my son")

class father(grandfather):
    def intro1(self):
        print("I am father of my son and son of my father")

class son(father):
    def intro2(self):
        print("I am son of my father and grandson of my grandfather")

obj1=son(10)

obj1.intro()
obj1.intro1()
obj1.intro2()


