# version code a52975dbbcb8
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vec import Vec
from vecutil import list2vec
from independence import is_independent
from itertools import combinations





## 1: (Task 7.7.1) Choosing a Secret Vector
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    #GF2 field elements s and t
    # output: a random 6 vector u such that a*u = s and b*u = t
    u = list2vec([randGF2() for x in range(6)])
    while a0 * u != s or b0 * u != t:
        u = list2vec([randGF2() for x in range(6)])

    return u


def get_vec():
    return list2vec([randGF2() for x in range(6)])

def test(L):
    return all(is_independent(list(sum(x,()))) for x in combinations(L,3))

vlist = [(a0,b0)]

while len(vlist) < 5:
    u = (get_vec(), get_vec())
    if test(vlist + [u]):
        vlist.append(u)

print(vlist)

## 2: (Task 7.7.2) Finding Secret Sharing Vectors
# Give each vector as a Vec instance
secret_a0 = list2vec([one, one,   0, one,   0, one])
secret_b0 = list2vec([one, one,   0,   0,   0, one])
secret_a1 = list2vec([one,one,one,0,0,one])
secret_b1 = list2vec([one,0,one,0,0,one])
secret_a2 = list2vec([one,0,one,0,one,one])
secret_b2 = list2vec([one,0,one,0,0,0])
secret_a3 = list2vec([one,one,one,one,0,0])
secret_b3 = list2vec([0,0,one,one,one,one])
secret_a4 = list2vec([0,one,0,one,one,0])
secret_b4 = list2vec([one,0,0,0,one,0])

vecs = [(secret_a0, secret_b0),(secret_a1,secret_b1),(secret_a2,secret_b2),(secret_a3,secret_b3),(secret_a4,secret_b4)]
print((all(is_independent(list(sum(x,()))) for x in combinations(vecs,3))))