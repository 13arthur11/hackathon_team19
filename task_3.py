from scipy.optimize import linprog
import numpy as np
def plot_minimized_hours(my_data):
    # cminimizes spare hours
    A = np.zeros((11,30),dtype = int)
    j=0
    for length in range(4,9):
        for i in range(12-length):
            A[i:(i+length),j] = -1
            j += 1
    B = -1*A
    A = A.tolist()
    c = [1 for i in range(30)]
    #h = [-122, -117,- 89,-23,-28,-31,-56,-98,-112,-110]
    # h = [-1,-5,-3,-1,-2,-1,-3,-5,-6,-3,-1]
    h = []
    for i in range(0, len(my_data)):
        h.append(-my_data[i])
    # h = my_data
    res = linprog(c, A_ub=A, b_ub=h, method="revised simplex")
    number_cour = res.x
    my_ata_2 = np.dot(B,number_cour)

    # plots 2 histograms
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot()
    plt.xlabel("Интервал Времени")
    x=["10.00", "11.00", "12.00", "13.00", "14.00", "15.00", "16.00", "17.00", "18.00", "19.00", "20.00"]

    xpos = np.arange(len(x))     
    plt.xticks(xpos, x)
    ax.bar(xpos-0.2, my_data, width=0.4, label="Входной прогноз")
    ax.bar(xpos+0.2, my_ata_2, width=0.4, label="Прогноз с поправкой на замощение")
    plt.legend()
    ax.grid()
    

plot_minimized_hours(my_data) # instead of my_data pass the array of nuber of deliverers at certain hours
