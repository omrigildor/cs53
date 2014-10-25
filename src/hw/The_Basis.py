# version code 031e89400b69
# Please fill out this stencil and submit using the provided submission script.

from GF2 import one
from math import sqrt, pi
from matutil import coldict2mat
from matutil import mat2coldict
from matutil import mat2rowdict
from solver import solve
from vecutil import list2vec
from vec import Vec
from submit import test_format



## 1: (Problem 5.14.1) Span of Vectors over R, A
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.
#
# For example, [1, 3, 5] would mean 1*[2,0,4,0] + 3*[0,1,0,1] + 5*[0,0,-1,-1]

rep_1 = [...]
rep_2 = [...]
rep_3 = [...]



## 2: (Problem 5.14.2) Span of Vectors over R, B
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

lin_comb_coefficients_1 = [...]
lin_comb_coefficients_2 = [...]
lin_comb_coefficients_3 = [...]
lin_comb_coefficients_4 = [...]



## 3: (Problem 5.14.3) Span of Vectors over GF2 A
# Use one from the GF2 module, not the integer 1.
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

gf2_rep_1 = [...]
gf2_rep_2 = [...]
gf2_rep_3 = [...]



## 4: (Problem 5.14.4) Span of Vectors over GF2 B
# Use one from the GF2 module, not the integer 1.
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

gf2_lc_rep_1 = [...]
gf2_lc_rep_2 = [...]
gf2_lc_rep_3 = [...]
gf2_lc_rep_4 = [...]



## 5: (Problem 5.14.5) Linear Dependence over R A
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

lin_dep_R_1 = [2,-1,-1]
lin_dep_R_2 = [28,-7,4]
lin_dep_R_3 = [-4138/1035, -35/207, 16/621, 1, 0]



## 6: (Problem 5.14.6) Linear Dependence over R B
# Please record your solution as a list of coefficients

linear_dep_R_1 = [1/3,-1/3,1]
linear_dep_R_2 = [2*pi*(sqrt(2)), sqrt(2), pi]
linear_dep_R_3 = [0,0,0,0]



## 7: (Problem 5.14.7) Superfluous vector
# Assign the COEFFICIENT of the vector to each variable.
# Assign sum_to to the vector that you are expressing as a linear combination
# of the other two.  Write the name of the vector as a STRING.  i.e. 'u' or 'w'

u = -1
v = 1
w = 0
sum_to = 'w'



## 8: (Problem 5.14.8) 4 linearly dependent vectors, every 3 are independent
# Please use the Vec class to represent your vectors

indep_vec_1 = list2vec([1,-1,0,0])
indep_vec_2 = list2vec([0,1,-1,0])
indep_vec_3 = list2vec([0,0,1,-1])
indep_vec_4 = list2vec([-1,0,0,1])



## 9: (Problem 5.14.9) Linear Dependence over GF(2) A
# Please give your solution as a list of coefficients of the linear combination

zero_comb_1 = [one, one, 0, one]
zero_comb_2 = [0,one,one,one]
zero_comb_3 = [one,one,0,0,one]



## 10: (Problem 5.14.10) Linear Dependence over GF(2) B
# Please give your solution as a list of coefficients of the vectors
# in the set in order (list the coefficient for v_i before v_j if i < j).

sum_to_zero_1 = [...]
sum_to_zero_2 = [...]
sum_to_zero_3 = [...]
sum_to_zero_4 = [...]



## 11: (Problem 5.14.11) Exchange Lemma for Vectors over $\R$
## Please express your answer as a list of ints, such as [1,0,0,0,0]

exchange_1 = [0,0,0,0,1]
exchange_2 = [0,0,0,1,0]
exchange_3 = [0,0,1,0,0]



## 12: (Problem 5.14.12) Exchange Lemma for Vectors over GF(2)
# Please give the name of the vector you want to replace as a string (e.g. 'v1')

replace_1 = 'v3'
replace_2 = 'v1'
replace_3 = 'v1'



## 13: (Problem 5.14.13) rep2vec
def rep2vec(u, veclist):
    '''
    Input:
        - u: a vector as an instance of your Vec class with domain set(range(len(veclist)))
        - veclist: a list of n vectors (as Vec instances)
    Output:
        vector v (as Vec instance) whose coordinate representation is u
    Example:
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> rep2vec(Vec({0,1,2}, {0:2, 1:4, 2:6}), [a0,a1,a2]) == Vec({'a', 'c', 'b', 'd'},{'a': 2, 'c': 6, 'b': 4, 'd': 0})
        True
    '''
    return coldict2mat(veclist) * u


## 14: (Problem 5.14.14) vec2rep
def vec2rep(veclist, v):
    '''
    Input:
        - veclist: a list of vectors (as instances of your Vec class)
        - v: a vector (as Vec instance) with domain set(range(len(veclist)))
             with v in the span of set(veclist).
    Output:
        Vec instance u whose coordinate representation w.r.t. veclist is v
    Example:
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> vec2rep([a0,a1,a2], Vec({'a','b','c','d'}, {'a':3, 'c':-2})) == Vec({0, 1, 2},{0: 3.0, 1: 0.0, 2: -2.0})
        True
    '''
    return solve(coldict2mat(veclist),v)


## 15: (Problem 5.14.15) Superfluous Vector in Python
def is_superfluous(L, i):
    '''
    Input:
        - L: list of vectors as instances of Vec class
        - i: integer in range(len(L))
    Output:
        True if the span of the vectors of L is the same
        as the span of the vectors of L, excluding L[i].

        False otherwise.
    Examples:
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
        >>> is_superfluous(L, 3)
        True
        >>> is_superfluous([a0,a1,a2,a3], 3)
        True
        >>> is_superfluous([a0,a1,a2,a3], 0)
        True
        >>> is_superfluous([a0,a1,a2,a3], 1)
        False
    '''
    if len(L) < 1:
        return False

    if len(L) == 1:
        return L[0].is_almost_zero()

    t = L.copy()
    p = t.pop(i)
    n = coldict2mat(t)
    u = p - n*solve(n,p)
    if u.is_almost_zero():
        return True


    return False


a0 = Vec({'a','b','c','d'}, {'a':1})
a1 = Vec({'a','b','c','d'}, {'b':1})
a2 = Vec({'a','b','c','d'}, {'c':1})
a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})

# print(is_superfluous([a0,a1,a2,a3], 3), True)
# print(is_superfluous([a0,a1,a2,a3], 3), True)
# print(is_superfluous([a0,a1,a2,a3], 0),True)
# print(is_superfluous([a0,a1,a2,a3], 1), False)

D = {'a','b','c','d'}
d0=Vec(D, {'a':1,'b':-1})
d1=Vec(D, {'c':-1,'b':1})
d2=Vec(D, {'c':1,'d':-1})
d3=Vec(D, {'a':-1,'d':1})
d4=Vec(D, {'b':1, 'c':1, 'd':-1})


# print((is_superfluous([d0,d1,d2,d3],3)),True)
# print(((is_superfluous([d0,d1,d2,d3],2))),True)
# print(((is_superfluous([d0,d1,d2,d3],1))),True)
# print(((is_superfluous([d0,d1,d2,d3],0))),True)
# print(((is_superfluous([d0,d1,d2,d3,d4],4))),True) #this case
# print(((is_superfluous([d0,d1,d2,d3,d4],3))),True)
# print(((is_superfluous([d0,d1,d2,d3,d4],2))),True)
# print(((is_superfluous([d0,d1,d2,d3,d4],1))),True)
# print(((is_superfluous([d0,d1,d2,d3,d4],0))),True)

v1 = Vec({0, 1, 2},{0: 0.1111111111111111, 1: 0.2857142857142857, 2: 0.6})
v2 = Vec({0, 1, 2},{0: 0.18181818181818182, 1: 0.17647058823529413, 2: 0.45454545454545453})
v3 = Vec({0, 1, 2},{0: 0.24963924963924963, 1: 0.5171886936592819, 2: 1.122077922077922})
# print(((is_superfluous([v1,v2,v3], 2))))
# print(((is_superfluous([v1],0))))
# print(((is_superfluous([Vec({0,1,2},dict())],0))))


## 16: (Problem 5.14.16) is_independent in Python
def is_independent(L):
    i = 0
    while True:
        if i >= len(L):
            return True

        elif is_superfluous(L,i):
            return False

        else:
            i+=1

vlist = [Vec({0, 1, 2},{0: 1}), Vec({0, 1, 2},{1: 1}), Vec({0, 1, 2},{2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 1}), Vec({0, 1, 2},{1: 1, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1})]
#print(is_independent(vlist), False)
#print(is_independent(vlist[:3]),True)
#print(is_independent(vlist[:2]), True)
#print(is_independent(vlist[1:4]),True)
#print(is_independent(vlist[2:5]),True)
#print(is_independent(vlist[2:6]),False)
#print(is_independent(vlist[1:3]),True)
# print(is_independent(vlist[5:]),True)

## 17: (Problem 5.14.17) Subset Basis
def subset_basis(T):
    i = 0
    A = T.copy()
    for x in T:
        if i >= len(A):
            break
        if is_superfluous(A,i):
            A.pop(i)
            i = i + 1

    return A



## 18: (Problem 5.14.18) Superset Basis Lemma in Python
def superset_basis(T, L):
    '''
    Input:
        - T: linearly independent list of Vec instances
        - L: list of Vec instances such that every vector in T is in Span(L)
    Output:
        Linearly independent list S containing all vectors (as instances of Vec)
        such that the span of S is the span of L (i.e. S is a basis for the span
        of L).1
    Example:
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
        >>> superset_basis([a0, a3], [a0, a1, a2]) == [Vec({'a', 'c', 'b', 'd'},{'a': 1}), Vec({'a', 'c', 'b', 'd'},{'b':1}),Vec({'a', 'c', 'b', 'd'},{'c': 1})]
        True
    '''
    k = T.copy()
    for i in L:
        k = k + [i]
        if not is_independent(k):
            k.remove(i)


    return k


a0 = Vec({'a','b','c','d'}, {'a':1})
a1 = Vec({'a','b','c','d'}, {'b':1})
a2 = Vec({'a','b','c','d'}, {'c':1})
a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})

#print(superset_basis([a0, a3], [a0, a1, a2]))

## 19: (Problem 5.14.19) Exchange Lemma in Python
def exchange(S, A, z):
    '''
    Input:
        - S: a list of vectors, as instances of your Vec class
        - A: a list of vectors, each of which are in S, with len(A) < len(S)
        - z: an instance of Vec such that A+[z] is linearly independent
    Output: a vector w in S but not in A such that Span S = Span ({z} U S - {w})
    Example:
        >>> S = [list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]]
        >>> A = [list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]]
        >>> z = list2vec([0,2,1,1])
        >>> exchange(S, A, z) == Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 1, 3: 0})
        True
    '''
    pass

