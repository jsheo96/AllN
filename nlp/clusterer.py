import torch
from sklearn.cluster import DBSCAN, KMeans
import numpy as np

class DBSCANClusterer:
    def __init__(self):
        pass
    def __call__(self, representative_embeddings): # input tensor n*768, output clustering (list)
        X = representative_embeddings
        clustering = DBSCAN(eps=0.4, min_samples=2, metric='cosine').fit(X)
        return clustering

if __name__ == '__main__':
    #X = torch.tensor([[1, 1], [2, 1], [1, 0],[4, 7], [3, 5], [3, 6]])
    
    X = torch.randn(10,768)
    #print(X.shape)
    clusterer = DBSCANClusterer()
    clustering = clusterer(X)
    print(clustering.labels_)
    exit()
