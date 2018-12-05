from utils import import_data, preprocess
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import re
from vect_utils import c_distance, simple_tokenizer
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from cluster import K_Means


filepath = 'data.txt'

data_as_lines, data_as_words = import_data(filepath)
l = preprocess(data_as_words)


vectorizer = TfidfVectorizer(
    use_idf=True, tokenizer=simple_tokenizer, 
    max_features=100,
    stop_words='english')

X = vectorizer.fit_transform(l)

from sklearn.decomposition import PCA
pca = PCA(n_components=50)
reduced = pca.fit_transform(X.todense())

t = reduced.transpose()
print len(t[0])
plt.scatter(t[3], t[4])
# plt.xlim(-0.08,0)
plt.show()
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(t[0], t[1], t[2])
# plt.show()

number_of_clusters = 5
km = KMeans(n_clusters=number_of_clusters)

km_own = K_Means(k=5)
km_own.fit(X.todense())
print km_own.get_clusters()

km.fit(X)
order_centroids = km.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()

centroids = []
for i in range(number_of_clusters):
    top_words = [terms[ind] for ind in order_centroids[i, :7]]
    centroids.append(' '.join(top_words))
    print "Cluster {}: {}".format(i, ' '.join(top_words)) 