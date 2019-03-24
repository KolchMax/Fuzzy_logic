import Paint as P
import math

'''
Тут следует быть внимательным при построении матрицы:
каждая 10-ая координата соответсвует индексу в таблице 
'''
field = \
[
    [45,  45,  30,  0,   0,   0,   0,   330, 315, 315],
    [45,  5,   45,  60,  70,  70,  30,  10,  350, 315],
    [60,  90,  95,  120, 95,  85,  60,  15,  0,   300],
    [90,  90,  150, 170, 130, 125, 80,  30,  355, 270],
    [90,  130, 175, 140, 180, 90,  45,  5,   340, 270],
    [90,  135, 185, 225, 270, 0,   40,  355, 315, 270],
    [90,  160, 210, 260, 300, 315, 350, 330, 310, 270],
    [120, 135, 190, 240, 265, 275, 300, 265, 270, 240],
    [135, 140, 180, 200, 215, 215, 225, 225, 250, 225],
    [135, 135, 150, 180, 180, 180, 180, 210, 225, 225]
]

#field = numpy.array(field1).transpose()

def function(coord, s):
    '''
    Функция принадлежности координаты coord полосе с номером s (s принадлежит 0 до 9, coord - 0:100)
    :param coord:
    :param s:
    :return:
    '''
    '''
    Если робот выходит за границы поля - он принадлежит крайней полосе
    '''
    if coord <= 0 and s == 0:
        return 1
    if coord >= 100 and s == 9:
        return 1
    if (coord - (s*10 - 5) > 0) and (coord - ((s+1)*10 + 5) <= 0):
        if coord <= (s*10+5):
            return abs(10 - abs(coord - s*10 - 5))/10
        else:
            return abs(10 - abs(coord - s*10 + 5))/10
    else:
        return 0

def function2(coord, s):
    if coord <= 0 and s == 0:
        return 1
    if coord >= 100 and s == 9:
        return 1
    if (coord - (s*10 - 5) > 0) and (coord - ((s+1)*10 + 5) <= 0):
        if coord <= (s*10+5):
            a = abs(10 - 2*abs(coord - s*10 - 5))/10
            if a > 1:
                return 1
            return a
        else:
            a = abs(10 - 2*abs(coord - s*10 + 5))/10
            if a > 1:
                return 1
            return a
    else:
        return 0

def function3(coord, s):
    if coord <= 0 and s == 0:
        return 1
    if coord >= 100 and s == 9:
        return 1
    if (coord - (s*10 - 5) > 0) and (coord - ((s+1)*10 + 5) <= 0):
        if coord <= (s*10+5):
            a = abs(10 - 3*abs(coord - s*10 - 5))/10
            if a > 1:
                return 1
            return a
        else:
            a = abs(10 - 3*abs(coord - s*10 + 5))/10
            if a > 1:
                return 1
            return a
    else:
        return 0

def get_alpha(coord_x, coord_y):
    '''
    Вычисляет угол по данным координатам
    :param coord_x:
    :param coord_y:
    :return:
    '''
    coeff = []    # коэфициенты
    corners = []  # углы
    b = 0
    a = 0
    for i in range(10):
        for j in range(10):
            '''принадлежность координаты x полосе i'''
            x = function2(coord_x, i)
            '''принадлежность координаты y полосе j'''
            y = function2(coord_y, j)
            c = x*y   #то, что Селедков говорил "Либо произведение, либо минимум из двух значений"
            if c != 0:
                print('x = ' + str(x) + ' i = ' + str(i) + ' y = ' + str(y) + ' j = ' + str(j))
                print('c = ' + str(c))
                corners.append(field[i][j])
                coeff.append(c)
    '''Цикл нормализующий углы для вчисления среднего между ними'''
    for i in range(len(corners)):
        k = i+1
        for j in range(k, len(corners)):
            if corners[j] - corners[i] > 180:
                corners[i] += 360
    '''
    Центр масс:
    alpha_result = sum(A_ij(coord)*alpha_ij)/sum(A_ij(coord))
    где alpha_result - результирующий угол в данной точке
        A_ij(coord) - функция принадлежности координаты квадрату i,j
        alpha_ij - угол в квадрате i, j
    '''
    for i in range(len(coeff)):
        b += coeff[i]
        a += coeff[i]*corners[i]
    return a/b

def get_next_coord(coord_x, coord_y, alpha_res):
    '''
    Вычисление следующей координаты по предыдущей координата и углу поворота
    :param coord_x:
    :param coord_y:
    :param alpha_res:
    :return:
    '''
    step = 3  # длина орезка
    next_coord_y = step*math.sin((alpha_res*math.pi)/180) + coord_y
    next_coord_x = step*math.cos((alpha_res*math.pi)/180) + coord_x
    return [next_coord_x, next_coord_y]

def main():
    start_pos = [50, 50]
    alpha = get_alpha(start_pos[0], start_pos[1])
    print('alpha = ' + str(alpha))
    next_pos = get_next_coord(start_pos[0], start_pos[1], alpha)
    print(next_pos)
    num_iter = 100  # количество отрисованных отрезков
    for i in range(num_iter):
        '''
        draw - отрисовка линии
        возвращает вторую точку
        '''
        start_pos = P.draw(start_pos, next_pos, png_file='func3.png')
        alpha = get_alpha(start_pos[0], start_pos[1])
        print('alpha = ' + str(alpha))
        next_pos = get_next_coord(start_pos[0], start_pos[1], alpha)
        print(next_pos)
    print('end')

main()
