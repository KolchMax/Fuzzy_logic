import index
import matplotlib.pyplot as plt


def build(png_file = 'test.png', xData = [], yData = [], color_num = 0):
    '''
    Построение графиков в файл .png
    :param data:
    :return:
    '''
    color = ['b', 'r', 'g']
    plt.figure(num=1, figsize=(24, 6))
    plt.xlabel('x', size=14)
    plt.ylabel('y', size=14)
    plt.plot(xData, yData, color=color[color_num], linestyle='-', label='Полоса '+str(color_num))
    plt.legend()
    plt.savefig(png_file, format='png')

for k in range(3):
    xData = list(0.1*i for i in range(300))
    print(xData)
    yData = []
    for x in xData:
        yData.append(index.func3(x, k))
    print(yData)
    print()
    build(png_file='test'+str(k)+'.png', xData=xData, yData=yData, color_num=k)
