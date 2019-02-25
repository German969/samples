from sklearn.neighbors import NearestNeighbors
import numpy as np

datos = [[0,0,0],[1,0,0],[0,2,0],[5,5,0],[5,6,0],[7,5,0],[0,7,0],[1,7,0],[0,9,0]]
individuo3 = [1,1,1,2,2,2,3,3,3]
individuo1 = [1,2,3,1,2,3,1,2,3]
individuo2 = [1,1,2,2,2,3,3,3,1]
k = 3
inter = []
for i in range(1, k + 1):
    indices = [index for index, x in enumerate(individuo2) if x == i]
    cluster = [x for index, x in enumerate(datos) if index in indices]

    nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(cluster)
    distances, indices = nbrs.kneighbors(cluster)
    distances = distances.tolist()
    maximo = max(distances)[1]
        
    inter.append(maximo)

media_inter = np.mean(inter)

print('distancias internas: '+str(inter))
print('media: '+str(media_inter))
print('maximo: '+str(max(inter)))

exter = []
for i in range(1, k + 1):
	print('cluster: '+str(i))
	indices = [index for index, x in enumerate(individuo2) if x == i]
	print('indices internos: '+str(indices))
	cluster = [x for index, x in enumerate(datos) if index in indices]
	print('cluster: '+str(cluster))

	indices2 = [index for index, x in enumerate(individuo2) if x != i]
	print('indices externos: '+str(indices2))
	cluster2 = [x for index, x in enumerate(datos) if index in indices2]
	print('cluster: '+str(cluster2))
	
	nbrs = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(cluster2)
	distances, indices = nbrs.kneighbors(cluster)
	distances = distances.tolist()
	print('distancia externa: '+str(distances))
	print('indices: '+str(indices))
	minimo = min(distances)
	print('minimo: '+str(minimo))
	
	exter.append(minimo)

media_exter = np.mean(exter)

print('distancias externas: '+str(exter))
print('media: '+str(media_exter))
print('minimo: '+str(min(exter)))

valor = media_exter / media_inter

print('valor evaluacion: '+str(valor))