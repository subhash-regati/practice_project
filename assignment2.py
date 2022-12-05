#Here functions of arithematic and logical  classes instance are created
class arithematic:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def addition(self):
        num3=self.num1+self.num2
        print(num3)
    def subtraction(self):
        num3 = self.num1 - self.num2
        print(num3)
    def multiply(self):
        num3 = self.num1 * self.num2
        print(num3)
    def division(self):
        num3 = self.num1 / self.num2
        print(num3)
class logical:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def AND_op(self):
        num3=self.num1 and self.num2
        print(num3)
    def OR_op(self):
        num3=self.num1 or self.num2
        print(num3)
    def NOT_op(self):
        num3= not (self.num1)
        print(num3)
print("arithematic addition of 9 and 7")
a1=arithematic(9,7)
l1=logical(9,1)
a1.addition()
print("logical AND operation of 9 and 1")
l1.AND_op()
print("logical NOT operation of 9")
l1.NOT_op()

