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

def func1(coord, s):
    '''
    треугольная функция
    :param coord:
    :param s:
    :return:
    '''
    if coord <= 0 and s == 0:
        return 1
    if coord >= 100 and s == 9:
        return 1
    a = (-abs(coord - s*10 - 5)+10)/10
    if a >= 0:
        return a
    else:
        return 0

def func2(coord, s):
    '''
    трапеция
    :param coord:
    :param s:
    :return:
    '''
    if coord <= 0 and s == 0:
        return 1
    if coord >= 100 and s == 9:
        return 1
    a = (-2*abs(coord - s*10 - 5)+15)/10
    if a >= 0:
        if a > 1:
            return 1
        else:
            return a
    else:
        return 0

def func3(coord, s, sigm=7):
    '''
    функция Гаусса
    :param coord:
    :param s:
    :param sigm:
    :return:
    '''
    if coord <= 0 and s == 0:
        return 1
    if coord >= 100 and s == 9:
        return 1
    a = math.exp(-pow((coord-10*s-5), 2)/sigm)
    if a < 0.00001:
        return 0
    return a

def get_alpha(coord_x, coord_y, function):
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
            x = function(coord_x, i)
            '''принадлежность координаты y полосе j'''
            y = function(coord_y, j)
            c = x*y   #конъюнкция
            if c != 0:
                print('x = ' + str(x) + ' i = ' + str(i) + ' y = ' + str(y) + ' j = ' + str(j))
                print('c = ' + str(c))
                corners.append(field[i][j])
                coeff.append(c)
    '''Цикл нормализующий углы для вчисления среднего между ними'''
    '''for i in range(len(corners)):
        k = i+1
        for j in range(k, len(corners)):
            if corners[j] - corners[i] > 180:
                corners[i] += 360'''

    sr = corners[0]
    for i in range(1, len(corners)):
        if sr - corners[i] > 180:
            corners[i] += 360
        elif corners[i]-sr > 180:
            corners[i] -= 360
        sr = (sr/i + corners[i])/(i + 1)

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

def get_next_coord(coord_x, coord_y, alpha_res, step):
    '''
    Вычисление следующей координаты по предыдущей координата и углу поворота
    :param coord_x:
    :param coord_y:
    :param alpha_res:
    :return:
    '''
    # длина орезка
    next_coord_y = step*math.sin((alpha_res*math.pi)/180) + coord_y
    next_coord_x = step*math.cos((alpha_res*math.pi)/180) + coord_x
    return [next_coord_x, next_coord_y]

def main(function, step, file_name, fig_id=1):
    start_pos = [50, 50]
    alpha = get_alpha(start_pos[0], start_pos[1], function)
    print('alpha = ' + str(alpha))
    next_pos = get_next_coord(start_pos[0], start_pos[1], alpha, step)
    print(next_pos)
    num_iter = 300//step  # количество отрисованных отрезков
    for i in range(num_iter):
        '''
        draw - отрисовка линии
        возвращает вторую точку
        '''
        start_pos = P.draw(start_pos, next_pos, png_file=file_name, fig_num=fig_id)
        alpha = get_alpha(start_pos[0], start_pos[1], function)
        print('alpha = ' + str(alpha))
        next_pos = get_next_coord(start_pos[0], start_pos[1], alpha, step)
        print(next_pos)
    print('end')

#main(function=func3, step=1, file_name='start_pos5050_func3_step1_v3.png')
