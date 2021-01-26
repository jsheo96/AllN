from sentence_transformers import SentenceTransformer
import torch
class Encoder:
    def __init__(self, model_path = './training_sts'):
        self.model_path = model_path
        self.embedder = SentenceTransformer(model_path)
    def __call__(self, sentences):
        return self.embedder.encode(sentences)

if __name__ == '__main__':
    encoder = Encoder()
    sentences =['안녕 나는 허지성','안녕하세요']
    while True:
        output = encoder(sentences)
    print(output.shape)

