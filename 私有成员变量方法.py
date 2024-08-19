class Phone:
    __voltage = 1

    def __init__(self, color, size, speed):
        self.color = color
        self.size = size
        self.speed = speed

    def __single_core(self):
        print("hello")


product_1 = Phone(color='blue', size=100, speed=1)
# product_1.single_core


