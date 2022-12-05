import math as m
class Euclidean:
    def __init__(self,x1,x2,y1,y2):
        self.x1=(x1)
        self.x2=(x2)
        self.y1=(y1)
        self.y2=(y2)
    def form(self):
        for i in range(0,4):

            print(m.sqrt(m.pow((self.x2[i]-self.x1[i]),2)+m.pow((self.y2[i]-self.y1[i]),2)))
    @classmethod
    def from_input(cls,inp):
        x1,x2,y1,y2=inp.split(',')
        return cls(x1,x2,y1,y2)
x1=[143.97385,144.27383,14.900002,15.200001]
x2=[-3.2746599,-2.9746597,10.35,10.65]
y1=[144.27383,143.97385,15.200001,14.900002]
y2=[ -3.2746599,-2.9746597,10.35,10.65]
input_1=Euclidean(x1,x2,y1,y2)

input_1.form()
