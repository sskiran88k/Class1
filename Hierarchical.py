class parent():
    def __init__(self,val):
        print(val)
    def intro(self):
        print("I have two children")
class child1(parent):
    def intro1(self):
        print("I am son of my parents")
class child2(parent):
    def intro2(self):
        print("I am daughter of my parents")

obj1=child1(5)
obj2=child2(10)

obj1.intro1()
obj2.intro2()
obj2.intro()