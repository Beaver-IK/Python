"""
# Принимаем значения матрицы и создаем ее, заполняя нулями.
list_size = [int(x) for x in input().split()]
n = list_size[0]
m = list_size[1]

matrix = [[0] * m for i in range(m)]

# Создаем счетчик чисел
counter = 1
# Начальное значение строки
x = 0
# Начальное значени столбца
y = -1
# Начальное значение сдвига по строкам
x_shift = 0
# Начальное значение сдвига по столбцам
y_shift = 1
# Делаем цикл, до тех пор, пока не закончатся значения для матрицы.
while counter <= n * m:
    # ставим условие, что цикл срабатывает, если только есть куда сдигаться во строкам, столбцам и ящейка еще не заполнена.
    if (0 <= x+x_shift < n) and (0 <= y+y_shift < m) and (matrix[x + x_shift][y + y_shift] == 0):
        # Икс принимает значение со сдвигом
        x += x_shift
        # Игрик тоже делает тоже самое
        y += y_shift
        # Матрица с индексами икс и игрик, принимает значение счетчика чисел.
        matrix[x][y] = counter
        # а счетчик чисел увеличивается на единицу
        counter += 1
        # Вот это самое главное. Тут мы меняем направление сдвигов, так чтоб все это двигалось по спирали. Вчитывайтесь и никайте.
    else:
        if y_shift == 1:
            x_shift = 1
            y_shift = 0
        elif x_shift == 1:
            y_shift = -1
            x_shift = 0
        elif y_shift == -1:
            x_shift = -1
            y_shift = 0
        elif x_shift == -1:
            x_shift = 0
            y_shift = 1

# Выводим матрицу
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
"""


n, m = map(int, input().split())
ma = [[0] * m for _ in range(n)]
x = 1
i, j = 0, 0
while x <= m * n:
    while j < m and ma[i][j] == 0: #вверх матрицы
        ma[i][j] = x
        x += 1
        j += 1
    i += 1
    j -= 1
    while i < n and ma[i][j] == 0: #право матрицы
        ma[i][j] = x
        x += 1
        i += 1
    j -= 1
    i -= 1
    while j >= 0 and ma[i][j] == 0: #низ матрицы
        ma[i][j] = x
        x += 1
        j -= 1
    i -= 1
    j += 1
    while i >= 0 and ma[i][j] == 0: #вверх матрицы
        ma[i][j] = x
        x += 1
        i -= 1
    j += 1
    i += 1

for i in range(n):
    for j in range(m):
        print(str(ma[i][j]).ljust(3), end='')
    print()
