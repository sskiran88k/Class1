class parent1():
    def greeting1(self):
        print("I am Father Class")

class parent2():
    def __init__(self,val):
        print(val)
    def greeting2(self):
        print("I am  Mother Class")

class child(parent1, parent2):
    print("I am the child class")

obj1=child(10)

obj1.greeting1()
obj1.greeting2()