import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def draw(point1, point2, png_file = 'picture.png', fig_num=1):
    '''
    Построение отрезка point1---point2 в файл .png
    файл не закрывается
    возвращает вторую точку
    :param data:
    :return:
    '''
    try:
        #fig, ax = plt.subplots()
        #  Добавляем подписи к осям:
        #ax.set_xlabel('x')
        #ax.set_ylabel('y')
        a = np.array([point1, point2])
        a = a.transpose()
        xData = a[0]
        yData = a[1]
        plt.figure(num=fig_num, figsize=(10, 10))
        plt.plot(xData, yData, color='b')
        plt.savefig(png_file)
        return point2
    finally:
        plt.savefig(png_file)

