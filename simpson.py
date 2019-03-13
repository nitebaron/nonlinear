import numpy as np
import math


#def f(x):
#	return (2/sqrt(np.pi))*np.sin(100*np.pi*x*)

def errf(x):
	return (2/np.sqrt(np.pi))*np.exp(-x**2)


def simpson(x,n):
	h = x/n
	
	for i in range(n):
		integrands = 2*errf(i*h)+4*errf((i-0.5)*h)


	integrand = h/6*(errf(0)+errf(n*h)+integrands)
	return integrand

print(simpson(0.2,1))