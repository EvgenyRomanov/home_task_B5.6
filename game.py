matrix = [['-' for i in range(3)] for j in range(3)]

def check(string):
    # проверка на выполнение условия победы в игре

    # проверяем столбцы
    def col(num, string):
        for i in range(3):
            if matrix[i][num] != string:
                return False
        return True
    
    for j in range(3):
        if col(j, string):
            return True
    
    # проверяем строки
    def row(num, string):
        for i in range(3):
            if matrix[num][i] != string:
                return False
        return True
            
    for j in range(3):
        if row(j, string):
            return True    
    
    
    # проверяем диагонали
    def diagonal_positive():
    #
     #
      #
        for i in range(3):
            for j in range(3):
                if i == j:
                    if matrix[i][j] != string:
                        return False
        return True
    
    
    def diagonal_negative():
      #
     #
    #
        for i in range(3):
            for j in range(3):
                if j == 2 - i:
                    if matrix[i][j] != string:
                        return False
        return True
    
    if diagonal_positive():
        return True
    
    if diagonal_negative():
        return True
    
    return False


def validator(x,y):
    # проверяем корректность введенных данных
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError()

    if not (0 <= x <= 2) or not (0 <= y <= 2):
        raise ValueError()
        
        

def print_matrix():
    # отображаем матрицу
    print()
    print('{:^2}{:^2}{:^2}{:^2}'.format('',0,1,2))
    for i in range(3):
        tmp = []
        for j in range(3):
            tmp.append(matrix[i][j])
        print('{:^2}{:^2}{:^2}{:^2}'.format(i,*tmp))

def change_matrix(x, y, string):
    matrix[x][y] = string
    
def check_string():
    # проверка на то, все ли ячейки заполнены нулями или крестиками
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == '-':
                return True
    return False

def check_string_players(x,y):
    # проверка на то, занята ячейка или нет
    if matrix[x][y] != '-':
        print("\nЯчейка уже занята!")
        return False
    return True
        
    
print_matrix()
while True:
    # в цикле получаем координаты от игроков
    
    while True:
        try:
            x1,y1 = list(map(int,input("Игрок 1 (X), введите координаты x и y через пробел: ").split()))
            validator(x1,y1)
            if check_string_players(x1,y1):
                break
        except ValueError:
            print("\nКоординаты должны быть целыми цислами от 0 до 2, введеными через пробел!")
    

    change_matrix(x1,y1,"X")
    print_matrix()
    if check("X"):
        print("\nИгрок 1 побеждает!")
        break
    if not check_string():
        print("\nИгра окончена!")
        break
    
    while True:
        try:
            x2,y2 = list(map(int,input("Игрок 2 (0), введите координаты x и y через пробел: ").split()))
            validator(x2,y2)
            if check_string_players(x2,y2):
                break
        except ValueError:
            print("\nКоординаты должны быть целыми цислами от 0 до 2, введеными через пробел!")
    
    
    change_matrix(x2,y2,"0")
    print_matrix()
    if check("0"):
        print("\nИгрок 2 побеждает!")
        break
    if not check_string():
        print("\nИгра окончена!")
        break
