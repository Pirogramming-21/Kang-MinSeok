import random

class Player:
    def __init__(self):
        self.name = self.__class__.__name__


    def brGame(self, num, opponent):
        while True:
            print("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ", end= ' ')
            count_input = input()
            if count_input.isdigit():  # 입력이 숫자인지 확인
                count = int(count_input)
                if 1 <= count <= 3:
                    break
                else:
                    print("1, 2, 3 중 하나를 입력하세요")
            else:
                print("정수를 입력하세요")

        for i in range(count):
            num += 1
            print(f"{self.name} {num}")


class Computer:
    def __init__(self):
        self.name = self.__class__.__name__

player = Player()
computer = Computer()

num = 0

