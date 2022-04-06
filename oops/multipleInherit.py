class Father:
    def __init__(self):
        super().__init__()  # this is used when multiple inheritance calling need to be done . this shoud be included in all class
        print("Father constroctor")

    def showF(self):
        print('from father calss')

class Mother:
    def __init__(self):
        super().__init__() # this is used when multiple inheritance calling need to be done . this shoud be included in all class
        print("Mother constroctor")
        
    def showM(self):
        print("from mother class")

class Son(Father,Mother):
    def __init__(self):
        super().__init__()
        print("son constroctor")
        
    def showS(self):
        print("from son Class")

s1 = Son();
s1.showS()
s1.showF();