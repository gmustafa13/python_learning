class Employee:
    def __init__(self,name,age,gender,add):
        self.name = name
        self.age = age
        self.gender = gender
        self.add = add

class Manager(Employee):
    def __init__(self,name,age,gender,add,skils,salaray):
        super().__init__(name,age,gender,add) # calling base class for name , age ,gender ,add
        self.skils = skils 
        self.salaray = salaray
    

m1 = Manager('Gulam',28,'Male','garden court','Js',100)
print(m1.name)
print(m1.salaray)



