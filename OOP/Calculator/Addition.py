class Addition:
    num1 = 0
    num2 = 0
    result = 0

    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2
        self.result = 0

    def Calculate(self):
        self.result = self.num1 + self.num2

    def GetResult(self):
        return self.result
