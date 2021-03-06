# version code 782534c2140b
# Please fill out this stencil and submit using the provided submission script.

# Copyright 2013 Philip N. Klein
from vec import Vec

#Test your Mat class over R and also over GF(2).  The following tests use only R.

# gets the item from the matrix
# can use the notation M[k] for the future
def getitem(M, k):
    return M.f[k] if k in M.f else 0

#set the item in the matrix to the value
def setitem(M, k, val):
    M.f[k] = val

# add two matrices
def add(A, B):
    assert A.D == B.D
    return Mat((A.D), {k:(A[k] + B[k]) for k in (A.f.keys() | B.f.keys())})

#multiply a scalar by a matrix
def scalar_mul(M, x):
    return Mat(M.D, {k:(x * M[k]) for k in M.f})

# returns true iff A is equal to B
def equal(A, B):
    assert A.D == B.D
    return all(A[k] == B[k] for k in (A.f.keys() | B.f.keys()))

# transpose a matrix
# A x B matrix becomes a B x A matrix
def transpose(M):
    return Mat((M.D[1], M.D[0]), {(k[1], k[0]): M[k] for k in (M.f.keys())})


# uses dot product notation
def matrix_vector_mul(M, v):
    assert M.D[1] == v.D
    return Vec(M.D[0], {i:sum([v[x] * M[i,x] for x in M.D[1]]) for i in M.D[0]})


# vector matrix multiplication outputs a vector using linear combination
def vector_matrix_mul(v, M):
    assert M.D[0] == v.D
    return Vec(M.D[1], {i:sum([v[x] * M[x,i] for x in M.D[0]]) for i in M.D[1]})


def matrix_matrix_mul(A, B):
    assert A.D[1] == B.D[0]
    # do first row by first column
    # rows x columns
    # iterate through A.D[0], A.D[1] through B.D[1], B.D[0]
    return Mat((A.D[0], B.D[1]), {(a,b):sum([A[a,i] * B[i,b] for i in A.D[1]]) for a in A.D[0] for b in B.D[1]})

################################################################################

class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self,other):
        if Mat == type(other):
            return matrix_matrix_mul(self,other)
        elif Vec == type(other):
            return matrix_vector_mul(self,other)
        else:
            return scalar_mul(self,other)
            #this will only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __sub__(a,b):
        return a+(-b)

    __eq__ = equal

    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None: rows = sorted(M.D[0], key=hash)
        if cols == None: cols = sorted(M.D[1], key=hash)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(str(c),colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(str(r), pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) +", " + str(self.f) + ")"


