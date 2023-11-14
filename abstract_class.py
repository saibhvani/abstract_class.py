from abc import ABC
class Employee(ABC):
    fName:str=""
    lName:str=""
    pay:float=10000
def sal(self):
     pass

def sal(self):
    pass

def setFullName(cls,fName:str,lName:str):
    cls.fName=fName
    cls.lName=lName

def getFullName(cls):
    return f'{cls.fName} {cls.lName}'
class perminentEmployee (Employee):
 def sal(self):
  return 12 *self.pay
emp = perminentEmployee()
emp.setFullName('sai','bhavani')
name = emp.getFullName()
sal = emp.sal()
print(name)
print(sal)








