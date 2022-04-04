class Student:
    ''' __init__ is same as contructor in other programming lunguage
    and self represent this key word or object of class '''
    def __init__(self, name, age, gender,email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

    def studentDetails(self):
        obj = {'name' :self.name , 'age' : self.age , 'gender': self.gender , 'email': self.email}
        return dict (obj)

class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def add(self , number):
        real = self.real + number.real
        imag = self.imag + number.imag
        # calling calss to genrate new object after adding both number 
        result = Complex(real,imag)
        return result;

class Triangle:
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b
        self.c = c

    def areaOfTrangle(self):
        return self.a* self.b* self.c;



