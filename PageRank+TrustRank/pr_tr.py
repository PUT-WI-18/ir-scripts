import numpy as np

q = 0.15
trusted_docs = [0,1]

def trust_rank(L: np.ndarray, q: float, trusted: []) -> np.ndarray:
    # array of trustness
    d = np.zeros([10], dtype=float)
    for i in trusted:
        d[i] = 1
    
    d_sum = np.sum(d)
    
    # normalize array of trustness
    tr = [v/d_sum for v in d]
    
    return page_rank(M, q, tr)

def page_rank(L: np.ndarray, q: float, d: np.ndarray = np.ones(10, dtype=float)) -> np.ndarray:
    # determine probability of visit by user. Uniform model used
    
    pr = np.zeros([len(L[0])], dtype=float)
    for i in range(10):
        pr[i] = 1/len(L[0])
        
    # initially prob of visiting is equal for each site - dividing by number of sites - 10
    # each iteration modify probs by summing vector dot product of previous iteration pr vector and row in M matrix
    # in this way one get average probability of visiting each page being on any other site
    # further modified by dumping factor - q preserving model from edge situations like dead-end - one site have prob of 1 and rest of them
    # being 0 as one site is self-linked and have non-other adjacent arcs
    
    for iter in range(ITERATIONS):
        pr_iter = np.zeros(10, dtype=float)
        for Li in range(10):
            pr_iter[Li] = q * d[Li] + (1-q) * np.sum(pr.dot(M[Li]))
        pr = pr_iter.copy()
    return pr / sum(pr)

def get_stochastic_matrix(L):
    # stochastic matrix - matrix of inversed number of links on each page
    # e.g. if page L1 is linked by page L2 and L2 has in total 2 links then M[L1][L2] is 1/2
    # tells what is a chance that user being on site L2 will wisit page L1
    M = np.zeros([10, 10], dtype=float)
    # number of outgoing links from each page
    c = np.zeros([10], dtype=int)
    
    for i in range(0, 10):
        c[i] = sum(L[i])
    
    for i in range(0, 10):
        for j in range(0, 10):
            if L[j][i] == 0: 
                M[i][j] = 0
            else:
                M[i][j] = 1.0/c[j]
    return M

L1  = [0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
L2  = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
L3  = [0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
L4  = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
L5  = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
L6  = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
L7  = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
L8  = [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
L9  = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
L10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

L = np.array([L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])

ITERATIONS = 100


    
print("Matrix L (indices)")
print(L)    

M = get_stochastic_matrix(L)

print("Matrix M (stochastic matrix)")
print(M)

print("PAGERANK")

page_rankk = page_rank(M, q)

for i in sorted(range(len(page_rankk)), key=lambda k: page_rankk[k], reverse=True):
    print('page index {} : Page Rank = {}'.format('L' + str(i + 1), page_rankk[i]))

print("TRUSTRANK")

trust_rankk = trust_rank(M, q, trusted_docs)
for i in sorted(range(len(trust_rankk)), key=lambda k: trust_rankk[k], reverse=True):
    print('page index {} : Trust Rank = {}'.format('L' + str(i + 1), trust_rankk[i]))