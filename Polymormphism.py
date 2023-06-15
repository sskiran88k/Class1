class INDIA():
    def introduction(self):
        print("India is a Highest Population Country in this world")
    def capital(self):
        print("India Capital is New Delhi")

class USA():
    def introduction(self):
        print("USA is a Less Population Country in this world")
    def capital(self):
        print("USA Capital is Washigton DC")

obj1=INDIA()
obj2=USA()

for i in (obj1, obj2):
    i.introduction()
    i.capital()