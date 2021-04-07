
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullname(self):

        return self.fname + " " + self.lname
    
    def email(self):

        f = self.fullname().replace(' ','')
        return f + "@gmail.com"

p1 = Person("sina","jamshidi")



