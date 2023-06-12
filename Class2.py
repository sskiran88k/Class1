class kiran():
    var1=0
    def __init__(self,var):
        kiran.var1+=1
        print(f"The Value is : {var}")
        print(f"The Value is : {kiran.var1}")

obj1=kiran(10)
obj2=kiran(90)
obj3=kiran(100)