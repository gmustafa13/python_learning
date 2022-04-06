class Car:
    def __init__(self,carType,noOfSeat,autometd):
        self.carType = carType
        self.noOfSeat = noOfSeat
        self.autometd = autometd

    def basicDetails(self):
        print(f'This Car is belong to {self.carType} category having {self.noOfSeat} and {self.autometd} features')

class Swift(Car):
    def __init__(self,carType,noOfSeat,autometd,color):
        super().__init__(carType,noOfSeat,autometd)
        self.color = color

    def carDetails(self):
        super().basicDetails()
        print(f"color is  {self.color}")

class Dealer(Swift):
    def __init__(self,carType,noOfSeat,autometd,color,dealerName):
        super().__init__(carType,noOfSeat,autometd,color)
        self.dealerName = dealerName

    def details(self):
        super().carDetails()
        print(f"Maruti suzuki {self.dealerName}")


b1 = Swift('hbase','5','semi-automated','black')
b1.carDetails()

d1 = Dealer('hbase1','6','semi-automated_','black_','Gulam')
d1.details()
