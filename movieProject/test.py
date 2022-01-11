class calc():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return a+b
    def mul(self):
        return a*b
    def division(self):
        return a/b
    def subt(self):
        return a-b

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
l=calc(a,b)

x=1
while x!=0:
    print("0. Exit")
    print("1. Add")
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    x=int(input("Enter choice:"))
    if x==1:
        print("Result: ",l.add())
    elif x==2:
        print("Result: ",l.subt())
    elif x==3:
        print("Result: ",l.mul())
    elif x==4:
        print("Result: ",l.division())
    elif x==0:
        print("Exiting!")
    else:
        print("Enter correct input")


