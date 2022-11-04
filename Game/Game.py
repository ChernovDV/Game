import os
import random


# Символы отображаемые в игровом поле
def get_symbol(val):
    if val == "0":
        return " "
    elif val == "1":
        return "X"
    return "O"

# Символ вводимый в игровое поле игроком
def invert_symbol(val):
    if val == " ":
        return "0"
    elif val == "X":
        return "1"
    return "2"

# Создаем игровое поле  с номерами полей по горизонтали и вертикали для удобства при выборе хода
rows = 3
cols = 3

def draw_table(table: str , size_board: tuple[int, int] = (rows , cols )):
    tmp = 1
    for idx, val in enumerate(table):

        if idx < rows + 1:
            print(f"|{idx}", end="")

        elif idx % size_board[1] == 0:
            print('|\n' + '-' + '-+' * (rows) + '--')
            print(f"|{tmp}", end="")
            tmp +=1

        else:
            print(f"|{get_symbol(val)}", end="")
    print("|")


# Ход игрока, добавляем символ на доску
def add_to_board(field, current_player, cols):

    while True:
        inp = input(f"Ход делает игрок '{current_player}' выберите строку и столбец\n").split()
        cur_row, cur_col = int(inp[0]), int(inp[1])
        if field[cols * cur_row + cur_col + cur_row] in ("1", "2"):
            print("Ячейка занята, выбери другую")
        else:
            break
    field[cols * cur_row + cur_col + cur_row] = invert_symbol(current_player)
    return field



# Очистка консоли
def clear_console():
    os.system("cls")


# Функция описывает кто победил

def who_win(table: str, curent_player:str, flag:bool, size_board: tuple[int, int] = (rows, cols)):

    # горизонталь
    for j in range(rows+2, (rows+1)*(cols+1), rows+1):
        for i  in range(j, j+rows):
            n = field[i]
            if field[i] == invert_symbol(curent_player):
                flag = True
            else:
                flag = False
                break
        if flag == True:
            break
    if flag == True:
        return flag

    # вертикаль
    for j in range(rows+2, 2*(rows+2)-1):
        for i  in range(j, (rows+1)*(cols+1), rows+1):
            n = field[i]
            if field[i] == invert_symbol(curent_player):
                flag = True
            else:
                flag = False
                break
        if flag == True:
            break
    if flag == True:
        return flag

    # диагональ №1
    for j in range(rows+2, 2*(rows+2)-1):
        k = 1
        for i  in range(j, (rows+1)*(cols+1), rows+1+k):

            if field[i] == invert_symbol(curent_player):
                flag = True
            else:
                flag = False
                break
        k += 1
        if flag == True:
            break
    if flag == True:
        return flag

# Функция нет свободных ячеек
def no_cell(field, curent_player:str, flag:bool,size_board: tuple[int, int] = (rows , cols )):
    count = 0
    for i in range((rows+1)*(cols+1)):
        if field[i] != invert_symbol(current_player):
            count += 1
        if count == rows*cols:
            flag = True

    if flag == True:
        return flag

# Game
rows = int(input ("Введите количество строк  "))
cols = int(input ("Введите количество столбцов  "))
field = ['0']*(rows*cols+rows+cols+1)
flag = True


while True:

    # Если нет свободных ячеек то ничья
    current_player = " "
    flag = no_cell(field, current_player, (rows, cols))
    if flag == True:
        clear_console()
        draw_table(field, (rows + 1, cols + 1))
        print("Стоп игра!")
        break
    # Последовательные ходы игроков
    current_player = "X"
    draw_table(field, (rows + 1, cols + 1))
    add_to_board(field, current_player, cols)

    flag = who_win(field, current_player, (rows, cols))
    if flag == True:
        clear_console()
        draw_table(field, (rows + 1, cols + 1))
        print("Победил игрок 'X'")
        break
    clear_console()


    current_player = "O"
    draw_table(field, (rows + 1, cols + 1))
    add_to_board(field, current_player, cols)

    flag = who_win(field, current_player, (rows, cols))
    if flag == True:
        clear_console()
        draw_table(field, (rows + 1, cols + 1))
        print("Победил игрок 'O'")
        break
    clear_console()



