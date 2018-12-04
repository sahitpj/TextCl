import numpy as np
import re
from scipy.sparse import csr_matrix

def c_distance(self, a, b):
    if a.shape[0] == b.shape[0]:
        r = 0.
        a = np.array(csr_matrix(a).todense()).T
        b = np.array(csr_matrix(b).todense())
        for i in xrange(a.shape[0]):
            r += a[i][0]*b[i][0]
        return r/((np.linalg.norm(a)*np.linalg.norm(b)))
    else:
        print 'Dimension mismatch'


def simple_tokenizer(str_input):
    words = re.sub(r"[^A-Za-z0-9\-]", " ", str_input).lower().split()
    return words