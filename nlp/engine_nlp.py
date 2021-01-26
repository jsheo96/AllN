# -*- coding: utf-8 -*-
import gc
from separator import Separator
from db_reader import DBReader
from encoder_kosenbert import Encoder
from summarizer import Summarizer
from clusterer import DBSCANClusterer
from sklearn.metrics import pairwise_distances
import tqdm
import time
import torch
import numpy as np
import pickle
import _sqlite3
import json
if __name__ == '__main__':
    # print('sadikljdfsl')
    db_reader = DBReader('/home/jsheo/AllN/news.db')
    raws = db_reader.contains('title', '카카오')
    representative_embeddings = []
    encoder = Encoder()
    separator = Separator()
    summarizer = Summarizer()
    news_indices = []
    news_embedding_data = {'indices':[], 'embeddings':[],'r_sentence':[]}
    for i in tqdm.tqdm(range(len(raws))):
        content = raws[i][3]
        try:
            sentences = separator(content)
            # if max([len(s) for s in sentences]) > 256:
            #     continue
            # if len(sentences) > 70:
            #     continue
            title = raws[i][2]
            sentences.append(title)
            embeddings = encoder(sentences)
            torch.cuda.empty_cache()
            representative_embedding, representative_index = summarizer(embeddings)
        except:
            continue
        representative_embeddings.append(representative_embedding)
        news_embedding_data['indices'].append(i)
        news_embedding_data['embeddings'].append(representative_embedding)
        news_embedding_data['r_sentence'].append(sentences[representative_index])
        news_indices.append(i)

    pickle.dump(news_embedding_data, open('news_embedding_data.pkl','wb'))
    # exit()
    news_embedding_data = pickle.load(open('news_embedding_data.pkl','rb'))
    news_indices = news_embedding_data['indices']
    representative_embeddings = news_embedding_data['embeddings']
    r_sentences = news_embedding_data['r_sentence']
    representative_embeddings = np.stack(representative_embeddings)
    clusterer = DBSCANClusterer()
    clustering = clusterer(representative_embeddings)

    clustering.labels_
    #print(news_indices)
    #print(clustering.labels_)
    labels = list(enumerate(clustering.labels_))
    # print(labels)
    #cluster_11 = [label[0] for label in labels if label[1]==21]
    #for i in cluster_11:
    #    print(r_sentences[i])

    #print(len(clustering.core_sample_indices_))
    #print(clustering.components_)

    clusters ={}
    for l in labels:

        if l[1] != -1:
            news_id = news_indices[l[0]]
            if l[1] not in clusters.keys():
                clusters[l[1]]={'r_sentence':r_sentences[l[0]],'news_id':[raws[news_id][4]],'date_i':raws[news_id][0],'date_f':raws[news_id][0], 'stock': '카카오'}
            else:
                clusters[l[1]]['news_id'].append(raws[news_id][4])
                clusters[l[1]]['date_f'] = raws[news_id][0]
    del_list = []
    # for k in clusters:
    #     if len(clusters[k]['news_id'])>5:
    #         del_list.append(k)
    #
    # for k in del_list:
    #     del clusters[k]

    print(clusters)
    print(clusters.keys())

    con = _sqlite3.connect('test.db')
    cursor = con.cursor()
    queries = []
    entities = []
    cursor.execute('SELECT issue_id from IssueDB')
    issue_ids = cursor.fetchall()
    max_id = max(issue_ids)
    for i, k in enumerate(clusters.values()):
        issue = k['r_sentence']
        date_i = k['date_i']
        date_f = k['date_f']
        stocks = k['stock']
        news = k['news_id']
        data = {'issue':issue, 'date_i':date_i, 'date_f':date_f, 'stocks':stocks, 'news':news}
        j = json.dumps(data,ensure_ascii=False)
        entities.append((i+max_id[0]+1,issue,j))
        # queries.append('INSERT INTO IssueDB VALUES ({}, {}, {})'.format(i, issue, data))
    cursor.executemany('INSERT INTO IssueDB VALUES (?,?,?)',entities)
    con.commit()
