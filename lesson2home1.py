while True:
    number = int(input('get number: '))
    if number > 0 and number < 10:
        print(number**2)
        break
    else:
        print('Введите новое число. Оно должно быть > 0 и < 10')

