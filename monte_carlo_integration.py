#The Monte Carlo method is can be used to integrate functions, even when the 
#functions are difficult or impossible to integrate analytically. The basis 
#of the method is to surround the function to be integrated by a simple volume 
#then generate sets of random numbers inside this volume and calculate the per-
#centage of these sets that satisfy the equation to be integrated. The method is 
#also used to calculate line and surface integrals by choosing random numbers along
#a line or surface rather than a volume.

#The error in the Monte Carlo method is inversely proportional to the square root 
#of the number of random numbers generated so to increase accuracy many random numbers 
#need to be generated. 

import numpy as np 


#calculate volume of an n dimensional spehere using the monte carlo method
#inputs: 
# n: number of random numbers generated 
# dim: dimension of sphere

def sphere_n_dim(n,dim):   
    satisfy = 0. #number of randomly generated points that are within the n dim. sphere
    for i in range(n):
        square_sum = 0. #volume of n dim. sphere
        for i in range(dim):
            square_sum = square_sum + np.power(np.random.rand(),2)
        if square_sum <= 1:
            satisfy = satisfy + 1
    return satisfy*np.power(2,dim)/n


#example run:
print(sphere_n_dim(500000,10))


#calculate the integral I = int(sin(ln(x+y+1)dS)) over the disk S = x^2+y^2 <= 0.25
#inputs:
# n: number of random numbers generated
def integral_surface(n):
	integral = 0.
	for i in range(1,n):
		x = np.random.rand()
		y = np.random.rand()
		if np.power(x,2)+np.power(y,2) <= 0.25:
			integral = integral + (np.sin(np.log(x+y+1)))/n

	return integral

#example run
print(integral_surface(1000000))
