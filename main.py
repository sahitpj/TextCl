from utils import import_data, preprocess
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import re
from vect_utils import c_distance, simple_tokenizer
from scipy.sparse import csr_matrix


filepath = 'data.txt'

data_as_lines, data_as_words = import_data(filepath)
l = preprocess(data_as_words)


vectorizer = TfidfVectorizer(
    use_idf=True, tokenizer=simple_tokenizer, 
    max_features=5000,
    stop_words='english')

X = vectorizer.fit_transform(l)


number_of_clusters = 10
km = KMeans(n_clusters=number_of_clusters)


km.fit(X)
order_centroids = km.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
centroids = []
for i in range(number_of_clusters):
    top_words = [terms[ind] for ind in order_centroids[i, :7]]
    centroids.append(' '.join(top_words))
    print "Cluster {}: {}".format(i, ' '.join(top_words)) 