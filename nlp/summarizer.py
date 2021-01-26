import networkx as nx
import numpy as np
import torch.nn as nn
import torch
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import cosine_similarity
class Summarizer:
    def __init__(self):
        self.cosine_similarity = nn.CosineSimilarity()

    def __call__(self, embeddings):
        # sim_mat = pairwise_distances(embeddings, embeddings, metric='cosine')
        # embeddings_tensor = torch.tensor(embeddings)
        # num_sentences = embeddings_tensor.shape[0]
        # sim_mat2 = [self.cosine_similarity(embeddings_tensor[i].unsqueeze(0).repeat_interleave(num_sentences, 0), embeddings_tensor) for i in range(num_sentences)]
        # sim_mat2 = torch.stack(sim_mat2)
        # sim_mat2 = sim_mat2.cpu().numpy()
        sim_mat3 = cosine_similarity(embeddings, embeddings)
        pagerank = nx.pagerank(nx.from_numpy_array(sim_mat3), max_iter=200)
        most_important_index = max(pagerank, key=pagerank.get)
        return embeddings[most_important_index], most_important_index

if __name__ == '__main__':
    summarizer = Summarizer()
    embeddings = torch.ones((32,768))
    representative_embedding = summarizer(embeddings)
    print(representative_embedding)
