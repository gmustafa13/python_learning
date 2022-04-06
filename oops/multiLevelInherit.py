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


b1 = Swift('hbase','5','semi-automated','black')
b1.carDetails()
