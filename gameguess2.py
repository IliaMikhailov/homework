import random
min = 1
max = 100
print('Загадайте число от 1 до 100 и запишите его на бумаге')
while True:
    print(min, max)
    number = random.randint(min, max)
    print(f' Компьютер выбрал число {number} ')
    User_answer = int(input(' Отгадал ли компьютер ваше число? 1. да,угадал 2. число больше 3. число меньше '))
    if User_answer == 1:
        print('Спасибо за игру')
        break
    elif User_answer == 2:
        min = number + 1
    else:
        max = number - 1


