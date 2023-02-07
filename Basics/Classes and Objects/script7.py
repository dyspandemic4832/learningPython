class Numberholder:
    def __init__(self,number):
        self.number = number

    def returnNumber(self):
        return self.number

var = Numberholder(7)
print(var.returnNumber())