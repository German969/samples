import numpy as np

datos = np.array([[2, 2], [4, 4], [4, 2], [5, 8], [5, 10], [7, 8], [11, 7], [13, 7], [13, 5]])
individuo1 = np.array([[2, 2], [5, 8], [11, 7]])
individuo2 = np.array([[2, 2], [4, 4], [13, 7]])
k = 3


def conjuntos_indices(individuo1, individuo2, datos, k):
    l_datos = datos.tolist()
	
	ind1 = np.ndarray(shape=[k], dtype=int)
    ind2 = np.ndarray(shape=[k], dtype=int)

    coord1 = np.ndarray(shape=individuo1.shape)
    coord2 = np.ndarray(shape=individuo1.shape)

    i = 0
    j = 0
    for el in individuo1:
        indexes = np.where(datos == el)
        index = indexes[0][0]
        ind1.put(i, index)

        coord1.put(i, datos[index])

        i += 1

    for el in individuo2:
        indexes = np.where(datos == el)
        index = indexes[0][0]
        ind2.put(j, index)

        coord2.put(j, datos[index])

        j += 1

    inter = np.intersect1d(ind1, ind2)
    xor = np.setxor1d(ind1, ind2)

    n_ind1_i = inter
    n_ind2_i = xor

    while (len(n_ind1_i) != k):
        np.append(n_ind1_i, np.random.choice(np.setdiff1d(xor, n_ind1_i)))

    while (len(n_ind2_i) != k):
        np.append(n_ind2_i, np.random.choice(np.setdiff1d(inter, n_ind2_i)))

    for i in range(0, k):
        coord1.put(i, datos[n_ind1_i[i]])
        coord2.put(i, datos[n_ind2_i[i]])

    return coord1, coord2


conjuntos_indices(individuo1, individuo2, datos, k)