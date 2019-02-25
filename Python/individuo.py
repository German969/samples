import numpy as np
import random

def generar_individuo(arr, dims, k, n):
	sal = np.empty(shape=(n, dims+1))
	i = 0
	for el in arr:
		n_el = np.empty(shape=(1, dims+1))
		for pos in range(0, dims):
			n_el.itemset(pos, el.item(pos))
		n_el.itemset(dims, random.randint(1, k))
		for att in range(0, len(n_el[0])):
			sal.itemset(att+(3*i), n_el[0][att])
		i += 1
	return sal
	
def gen_ind(k, n):
	sal = np.random.randint(1, high=4, size=(n,1))
	return sal

arr = np.random.randint(9, size=(30, 2))
dims = 2
k = 3
n = 30

#print(arr)

print(gen_ind(k, n))

