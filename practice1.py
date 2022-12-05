class employee:
    no_of_emp=0
    percent=1.04
    def __init__(self,first,last,pay):
        self.fname=first
        self.lname=last
        self.pay=pay
        self.mail=self.fname+self.lname+'@veoneer.com'
        employee.no_of_emp+=1
    def raise_amount(self):
        self.pay=int(self.pay*self.percent)
    def fullname(self):
        return '{}.{}'.format(self.fname,self.lname)
    def __repr__(self):
        return '{} ' '{} ' '{} '.format(self.fname,self.lname,self.pay)
    def __str__(self):
        return '{}-{}'.format(self.fullname(),self.mail)
    def __add__(self, other):
        return self.pay+other.pay
    @classmethod
    def amount_raise(cls,amount):
        cls.percent=amount
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay =emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def work_day(day):
        if day.weekday()==5 or day.weekday()==6:
            return True
        return False
class developer(employee):
    percent = 1.10
    def __init__(self,first,last,pay,p_lang):
        super().__init__(first,last,pay)
        self.p_lang=p_lang
class manager(employee):
    def __init__(self,first,last,pay,Employees=None):
        super().__init__(first,last,pay)
        if Employees is None:
            self.Employees= []
        else:
            self.Employees=Employees
    def add_emp(self,emp):
        if emp not in self.Employees:
            self.Employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.Employees:
            self.Employees.remove(emp)
    def print_emp(self):
        for emp in self.Employees:
            print('---->',emp.fullname())





e1=developer('subhash','regati',30000,'python')
e2=developer('sam','jack',50000,'java')
e3=manager('test','engineer',90000,[e1])
e3.add_emp(e2)
e3.print_emp()
print(e1.pay)
employee.amount_raise(1.10)
e1.raise_amount()
new_emp_1=employee.from_string("subhash-regati1-32123")
print(e1.pay)
print(e2.mail)
k=e2.fullname()
print(k)
print(new_emp_1.pay)
print(e1.no_of_emp)
import datetime
my_date=datetime.date(2022,9,1)
work_day=employee.work_day(my_date)
print(work_day)
print(e1.p_lang)
print(isinstance(e1,employee))
print(issubclass(manager,employee))
print(e1)
print(int.__add__(1,2))
print(str.__add__('1','2'))
print(e1+e2)