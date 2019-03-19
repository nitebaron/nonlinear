#this script finds the percentage constituents of a sample, originally all Uranium-234,
#as it #decays through various daughter reactions to Lead-206. The method used is a 
#Monte Carlo approach, with numerical analysis.
#consider the following radioactive chain:
#				  half-life 
#234U  -> 230Th    2.5x10^5 years
#230Th -> 226Ra    8x10^4 years
#226Ra -> 222Rn    8x10^4 years
#222Rn -> 206Pb    4 days, stable

import numpy as np 
import matplotlib.pyplot as plt

def simulate_decay(init_population, half_lives, t):
	lambdas = np.ones(len(half_lives))
	for i in range(len(half_lives)):
		lambdas[i] = np.log(2)/half_lives[i]

	population = init_population
	population_array = np.zeros(len(t))
	delta_t = 1000.


	for t in range(len(t)):
		population_array[t] = population[1] 

		for j in range(len(half_lives)):
			for i in range(population[j]):
				if np.random.rand() < 1-np.exp(-lambdas[j]*delta_t):
					population[j] = population[j]-1
					population[j+1] = population[j+1]+1

	t = np.linspace(0,1000000,1000)
	#print(init_population[0])
	analytic1 = 1000*np.exp(-lambdas[0]*t)
	analytic2 = 1000*(lambdas[0]/(lambdas[1]-lambdas[0]))*(np.exp(-lambdas[0]*t)-np.exp(-lambdas[1]*t))
	#print(population_array)
	
	plt.plot(t,population_array,'r')
	plt.plot(t,analytic2,'b')
	#axes = plt.gca()
	#axes.set_xlim([0,1000000])
	#axes.set_ylim([0,1000])
	#axes.set_ylim([0,1200])
	plt.show()

	return population


#example use

#assume a pure 234U sample initially
init_population = [1000, 0, 0, 0, 0]
half_lives = [250000, 80000, 1620, 4./365.]
t = np.linspace(0,1000000,1000)
population = simulate_decay(init_population, half_lives, t)
print(population)
