import numpy as np

def generar_individuo(arr, dims, k):
	sal = np.array([])
	for el in arr:
		n_el = np.array([])
		for pos in range(0, dims):
			np.vstack((n_el,el[pos]))
		n_el[dims] = random.randint(1, k)
		sal = np.vstack((sal, n_el))
	return sal

A = np.array([])
B = np.array([3,5])
C = np.array([7,9])
E = np.array([1,6])

D = np.vstack((A,B))
D = np.vstack((D,C,E))

print(D)

# generar_individuo(D,2,2)