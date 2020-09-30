class Employee():
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
h = Employee('suhas','deshmukh',10000)
r = Employee('sujata','kulkarni',12000)

print(h.fname,r.salary)