import random

RandomNumber = random.randint(1, 100)
UserNumber = 0

print("Угадай число от 1 до 100")

while UserNumber != RandomNumber:
    UserNumber = int(input())
    if UserNumber > RandomNumber:
        print("Число меньше")
    elif UserNumber < RandomNumber:
        print("Число больше")
    else:
        print("Вы угадали!!! Это число " + str(RandomNumber))
        break
