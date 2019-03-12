import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative

# solving non linear equations using the
# bisection method: repeated halving of the interval. pick two points x1
# and x2 such that f(x1) and f(x2) have opposite signs. Then find the
# midpoint x3 = (x1+x2)/2, and test its sign, then replace either x1 or x2 with this
# midpoint depending on the sign of the midpoint (so that we'd get closer to the root) 

# newton raphson method: pick a point x1 near the root of interest, then x2
# is given by x2 = x1 - f(x1)/f'(x1)
# WARNING: if you take a wrong initial point x1, this method might take you further
# away from the root.

def f(x):
	return 3*math.exp(-x)-x+3

def bisection(x1,x2):
	
	x3 = (x1+x2)/2
	#print(x3)

	while abs(f(x3)) > 0.01:
		#sanity check
		#print(abs(f(x3)))
		#print(x3)
		#print(f(x3))

		if f(x1)*f(x2) >= 0:
			print("you need one number below, and another above 0, as your root is at 0, dumb dog")
			break

		if f(x3)*f(x2) < 0:
			x1 = x3
			#print(x1)
			
		else:
			x2 = x3
		
		x3 = (x1+x2)/2

	return "meh"


x1 = 1.0
x2 = 15.0
x = 4.0
#print(f(3))
result = bisection(x1,x2)
#print(result)


def newton_raphson(x):

	x = x-f(x)/derivative(f, x, dx=1e-6)

	while abs(f(x)) > 0.01:
		x = x-f(x)/derivative(f, x, dx=1e-6)
		print(x)
	return "meh"


print(newton_raphson(x))

