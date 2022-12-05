from math import sqrt


class Euclidean:
    def __init__(self,x1,x2,y1,y2):
        self.x1=float(x1)
        self.x2=float(x2)
        self.y1=float(y1)
        self.y2=float(y2)
    def form(self):

        print(sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2))
    @classmethod 
    def from_input(cls,inp):
        x1,x2,y1,y2=inp.split(',')
        return cls(x1,x2,y1,y2)
inp_1='143.97385,-3.2746599,144.27383,-3.2746599'
inp_2='144.27383,-2.9746597,143.97385,-2.9746597'
inp_3='14.900002,10.35,15.200001,10.35'
inp_4='15.200001,10.65,14.900002,10.65'
input_1=Euclidean.from_input(inp_1)
input_2=Euclidean.from_input(inp_2)
input_3=Euclidean.from_input(inp_3)
input_4=Euclidean.from_input(inp_4)
input_1.form()
input_2.form()
input_3.form()
input_4.form()