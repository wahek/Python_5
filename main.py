# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""
import random
candies = 28
sweets = 150
coin = random.randint(1,2)
if coin == 1:
    print('Первый ход за компьютером')
else:
    print('Вы ходите')
while sweets > 57:
    if coin == 2:
        candies = int(input('Введите количество которые хотите забрать: '))
        while candies < 1 or candies > 28:
            candies = int(input('Введите количество от 1 до 28: '))
        sweets = sweets - candies
        coin -= 1
        print(f'Остаток конфет: {sweets}')
    else:
        candies = sweets // 29
        if candies < 5:
            print(f'ИИ забирает {candies} конфеты')
        else:
            print(f'ИИ забирает {candies} конфет')
        sweets -= candies
        print(f'Остаток конфет: {sweets}')
        coin += 1
while sweets > 28:
    if coin == 1:
        candies = 1
        while sweets > 29:
            sweets -= 1
            candies += 1
        print(f'ИИ забирает {candies} конфет')
        print(f'Остаток конфет: {sweets}')
        coin += 1
    if coin == 2:
        candies = int(input('Введите количество которые хотите забрать: '))
        while candies < 1 or candies > 28:
            candies = int(input('Введите количество от 1 до 28: '))
        sweets = sweets - candies
        coin -= 1
        print(f'Остаток конфет: {sweets}')
if coin == 1:
    print(f'Компьютер забрал все конфеты игрока, ИИ = 150 конфет')
else:
    print(f'игрок забрал все конфеты компьютера, игрок = 150 конфет')
