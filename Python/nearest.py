from sklearn.neighbors import NearestNeighbors
import numpy as np


datos = np.array([[2, 2], [4, 4], [4, 2], [5, 8], [5, 10], [7, 8], [11, 7], [13, 7], [13, 5]])
clasificacion = np.array([[1],[1],[1],[2],[2],[2],[3],[3],[3]])
clasificacion_mal = np.array([[1],[2],[3],[1],[2],[3],[1],[2],[3]])

def clusters_division(datos,clasificacion):
	clusters = []
	for k in np.unique(clasificacion):
		new = [i for i, e in enumerate(clasificacion) if e == k]
		clusters.append(new)
	return(clusters)
		
clusters = clusters_division(datos,clasificacion)

def nearest_neighbors(datos, clusters):
	
# X = np.array([[2, 2], [4, 4], [4, 2], [5, 8], [5, 10], [7, 8]])
# nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
# distances, indices = nbrs.kneighbors(X)