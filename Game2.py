import os

rows = int(input("Введите количество строк  "))
cols = int(input("Введите количество столбцов  "))

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


def draw_field(field:list, size_board: tuple[int, int] = (rows , cols )):

    for idx, val in enumerate(field):
        if idx == 0:
            print(f"|{get_symbol(val)}", end="")

        elif idx % size_board[1] == 0:
            print('|\n' + '-' + '-+' * (size_board[1]-1) +'--')
            print(f"|{get_symbol(val)}", end="")

        else:
            print(f"|{get_symbol(val)}", end="")
    print("|")

# Ход игрока, добавляем символ на доску
def add_to_board(field:list, current_player, cols):
    while True:
        inp = input(f"Куда будет ставить игрок {current_player} строка столбец\n").split()

        cur_row, cur_col = int(inp[0]), int(inp[1])
        if field[cols * cur_row + cur_col] in ("1", "2"):
            print("Ячейка занята, выбери другую")
        else:
            break
    field[cols * cur_row + cur_col] = invert_symbol(current_player)
    return field

# Очистка консоли
def clear_console():
    os.system("cls")

# Функция нет свободных ячеек
def no_cell(field:list ,size_board: tuple[int, int] = (rows , cols )):
    tmp = True
    for i in range(size_board[0]*size_board[1]):
        if field[i] == "0":
           tmp = False

    if tmp == True:
        print("Стоп игра.Ничья!")

# Функция описывает кто победил


def who_win(field:list, current_player, size_board: tuple[int, int] = (rows, cols)):
    # горизонталь
    flag = False
    count = 0
    for i in range(0,size_board[0]*size_board[1],rows):
        for j in range(i,i+rows):
            if field[j] == invert_symbol(current_player):
                flag = True
                count += 1
            else:
                flag = False
        if flag == True and count == rows:
            return flag

    # вертикаль и диагональ
    flag = False
    count = 0
    for i in range(0, rows):
        for j in range(i, size_board[0] * size_board[1], rows):
            if field[j] == invert_symbol(current_player):
                flag = True
                count += 1
            else:
                flag = False
        if flag == True and count == rows:
            return flag
    # диагональ

#////////////////////////////////////Game/////////////////////////////////////////////////////
def game ():
    # Задаём первого игрока
    current_player = "X"
    # Задаём размер игрового поля

    field = ["0"] * (rows * cols)

    while True:
       # Вывести игровое поле в консоль
        draw_field(field, (rows, cols))

        # Игрок делает ход
        add_to_board(field, current_player, cols)

       # Проверка на наличие свободных ячеек
        no_cell(field, (rows, cols))

        # Проверка на победителя
        win = who_win(field, current_player, (rows, cols))
        if win:
            clear_console()
            print(f"Победил {current_player}")
            draw_field(field, (rows, cols))
            break
        else:
        # Переход хода
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
            clear_console()

# Main
game()

