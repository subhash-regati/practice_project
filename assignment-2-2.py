class ort_dist:

    def __init__(self,A,B,C,x1,y1):
        self.A=int(A)
        self.B=int(B)
        self.C=int(C)
        self.x1=int(x1)
        self.y1=int(y1)
    def form(self):
        print("distance for data ")
        print((self.A*self.x1)+(self.B*self.y1+self.C)/(self.A**2+self.B**2)**0.5)
    @classmethod
    def from_input(cls,inp):
        A,B,C,x1,y1=inp.split(',')
        return cls(A,B,C,x1,y1)
inp_1='2,5,10,2,3'
inp_2='5,3,6,6,9'
input_1=ort_dist.from_input(inp_1)
input_2=ort_dist.from_input(inp_2)
input_1.form()
input_2.form()
