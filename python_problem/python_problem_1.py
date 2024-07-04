import random

class Player:
    def __init__(self):
        self.name = self.__class__.__name__

    print("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ", end= ' ')
    count_input = input()


class Computer:
    def __init__(self):
        self.name = self.__class__.__name__

player = Player()
computer = Computer()

num = 0

