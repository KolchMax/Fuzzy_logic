import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def draw(point1, point2, png_file = 'picture.png'):
    '''
    Построение отрезка point1---point2 в файл .png
    файл не закрывается
    возвращает вторую точку
    :param data:
    :return:
    '''
    try:
        a = np.array([point1, point2])
        a = a.transpose()
        xData = a[0]
        yData = a[1]
        plt.figure(num=1, figsize=(10, 10))
        plt.plot(xData, yData, color='b')
        plt.savefig(png_file)
        return point2
    finally:
        plt.savefig(png_file)

