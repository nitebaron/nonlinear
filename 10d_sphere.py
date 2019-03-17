#calculate volume of a 10 dimensional spehere using the monte carlo method

import numpy as np 

def sphere10d(n):   
    satisfy = 0.
    for i in range(n):
        square_sum = 0.
        for i in range(10):
            square_sum = square_sum + np.power(np.random.rand(),2)
        if square_sum <= 1:
            satisfy = satisfy + 1
    return satisfy*1024/n





print(sphere10d(500000))



    #np.power(x1,2)+np.power(x2,2)+np.power(x3,2)+np.power(x4,2)+np.power(x5,2)+np.power(x6,2)+np.power(x7,2)+np.power(x8,2)+np.power(x9,2)+np.power(x10,2) <= 1