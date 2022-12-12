import random

cell = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second = input('Введите ваше имя: '), input('Введите имя противника: ')
coin = random.randint(1, 2)
if coin == 1:
    print(f'Первый ход за {first}, ходит х')
else:
    print(f'Первый ход за {second}, ходит 0')


def board(cell):
    print(f'{cell[0]} | {cell[1]} | {cell[2]}')
    print('---------')
    print(f'{cell[3]} | {cell[4]} | {cell[5]}')
    print('---------')
    print(f'{cell[6]} | {cell[7]} | {cell[8]}')


def first_win(cell):
    if (cell[0] == 'X' and cell[1] == 'X' and cell[2] == 'X') or (
            cell[3] == 'X' and cell[4] == 'X' and cell[5] == 'X') or (
            cell[6] == 'X' and cell[7] == 'X' and cell[8] == 'X'):
        print(f'{first} выиграл по горизонтали. Поздравляем!!!')
        board(cell)
        exit()
    elif (cell[0] == 'X' and cell[3] == 'X' and cell[6] == 'X') or (
            cell[1] == 'X' and cell[4] == 'X' and cell[7] == 'X') or (
            cell[2] == 'X' and cell[5] == 'X' and cell[8] == 'X'):
        print(f'{first} выиграл по вертикали. Поздравляем!!!')
        board(cell)
        exit()
    elif (cell[0] == 'X' and cell[4] == 'X' and cell[8] == 'X') or (
            cell[2] == 'X' and cell[4] == 'X' and cell[6] == 'X'):
        print(f'{first} выиграл по диагонали. Поздравляем!!!')
        board(cell)
        exit()


def second_win(cell):
    if (cell[0] == 0 and cell[1] == 0 and cell[2] == 0) or (cell[3] == 0 and cell[4] == 0 and cell[5] == 0) or (
            cell[6] == 0 and cell[7] == 0 and cell[8] == 0):
        print(f'{second} выиграл по горизонтали. Поздравляем!!!')
        board(cell)
        exit()
    elif (cell[0] == 0 and cell[3] == 0 and cell[6] == 0) or (cell[1] == 0 and cell[4] == 0 and cell[7] == 0) or (
            cell[2] == 0 and cell[5] == 0 and cell[8] == 0):
        print(f'{second} выиграл по вертикали. Поздравляем!!!')
        board(cell)
        exit()
    elif (cell[0] == 0 and cell[4] == 0 and cell[8] == 0) or (cell[2] == 0 and cell[4] == 0 and cell[6] == 0):
        print(f'{second} выиграл по диагонали. Поздравляем!!!')
        board(cell)
        exit()


count = 0  # количество ходов
while count < 9:
    if coin == 1:
        board(cell)
        stap = int(input(f'{first} вводи ячейку куда хочешь ходить: '))
        if 0 < stap < 10:
            if cell[stap - 1] != 0 and cell[stap - 1] != 'X':
                cell[stap - 1] = 'X'
                count += 1
                coin += 1
                first_win(cell)
            else:
                print('Ячейка занята')
        else:
            print('Такой ячейки не существует')
    if coin == 2:
        board(cell)
        stap = int(input(f'{second} вводи ячейку куда хочешь ходить: '))
        if 0 < stap < 10:
            if cell[stap - 1] != 0 and cell[stap - 1] != 'X':
                cell[stap - 1] = 0
                count += 1
                coin -= 1
                second_win(cell)
            else:
                print('Ячейка занята')
        else:
            print('Такой ячейки не существует')
if count == 9:
    print('Ничья')
    board(cell)
