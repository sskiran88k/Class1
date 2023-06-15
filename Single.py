class parent():
    def __init__(self,val):
        print(f"The value is : {val} ")
    def introduction(self):
            print("I am the Parent Class")

class child(parent):
    def introduction(self):
        print("I am the Child Class")

obj1=parent(100)
obj1.introduction()

obj2=child(50)
obj2.introduction()
