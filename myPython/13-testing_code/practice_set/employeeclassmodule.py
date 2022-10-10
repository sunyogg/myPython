class Employee:

    def __init__(self,fname,lname,pay):
        self.fname = fname.title()
        self.lname = lname.title()
        self.pay = pay


    def raise_pay(self,value=5000):
        self.pay += value





