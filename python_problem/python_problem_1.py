class Player:
    def __init__(self):
        self.name = self.__class__.__name__


class Computer:
    def __init__(self):
        self.name = self.__class__.__name__

player = Player()
computer = Computer()

num = 0

