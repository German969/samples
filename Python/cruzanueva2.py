import numpy as np
import random

datos = np.array([[2, 2], [4, 4], [4, 2], [5, 8], [5, 10], [7, 8], [11, 7], [13, 7], [13, 5]])
individuo1 = np.array([[2, 2], [5, 8], [11, 7]])
individuo2 = np.array([[2, 2], [4, 4], [13, 7]])
k = 3

def conjuntos_indices(individuo1, individuo2, datos, k):
	datos = datos.tolist()
	
	individuo1 = individuo1.tolist()
	individuo2 = individuo2.tolist()
	
	ind1 = []
	ind2 = []
	
	coord1 = []
	coord2 = []

	for el in individuo1:
		index = datos.index(el)
		ind1.append(index)

		coord1.append(datos[index])

	for el in individuo2:
		index = datos.index(el)
		ind2.append(index)

		coord2.append(datos[index])

	inter = [x for x in ind1 if x in ind2]
	xor = [a for a in ind1+ind2 if (a not in ind1) or (a not in ind2)]

	n_ind1_i = inter
	n_ind2_i = xor
	
	x = inter
	y = xor

	while (len(n_ind1_i) != k):
		el1 = random.choice(y)
		y.remove(el1)
		n_ind1_i.append(el1)

	while (len(n_ind2_i) != k):
		el1 = random.choice(x)
		x.remove(el1)
		n_ind2_i.append(el1)
		
	n_coor1 = []
	n_coor2 = []
		
	for i in range(0, k):
		n_coor1.append(datos[n_ind1_i[i]])
		n_coor2.append(datos[n_ind2_i[i]])

	return coord1, coord2
	
conjuntos_indices(individuo1, individuo2, datos, k)