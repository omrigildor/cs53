# version code a3133383da20
# Please fill out this stencil and submit using the provided submission script.

# Copyright 2013 Philip N. Klein
#Includes all code for the functions, i.e. solution to part of hw01

# getitem - takes in a vector and  a key
# returns the value of that key if it exists else 0
def getitem(v,k):
    return v.f[k] if k in v.f else 0

# setitem - vector, v key, k value, v
# set the item of key to val
def setitem(v,k,val):
    v.f[k] = val

# equal two vectors
def equal(u,v):
    assert u.D == v.D

    return all(u[k] == v[k] for k in u.D)

# add two vectors
def add(u,v):
    assert u.D == v.D
    return Vec(u.D, {x:(u[x] + v[x]) for x in u.D})

#dot product two vectors
def dot(u,v):
    assert u.D == v.D
    return sum([u[x] * v[x] for x in u.D])

#scalar mult two vectors
def scalar_mul(v, alpha):
    return Vec(v.D, {x:(v[x] * alpha) for x in v.D})

# negation of a vector
def neg(v):
    return Vec(v.D, {x:(-1 * v[x]) for x in v.D})

###############################################################################################################################

class Vec:
    """
    A vector has two fields:
    D - the domain (a set)
    f - a dictionary mapping (some) domain elements to field elements
        elements of D not appearing in f are implicitly mapped to zero
    """
    def __init__(self, labels = set(), function = {}):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    __neg__ = neg
    __rmul__ = scalar_mul #if left arg of * is primitive, assume it's a scalar

    def __mul__(self,other):
        #If other is a vector, returns the dot product of self and other
        if isinstance(other, Vec):
            return dot(self,other)
        else:
            return NotImplemented  #  Will cause other.__rmul__(self) to be invoked

    def __truediv__(self,other):  # Scalar division
        return (1/other)*self

    __add__ = add

    def __radd__(self, other):
        "Hack to allow sum(...) to work with vectors"
        if other == 0:
            return self

    def __sub__(a,b):
        "Returns a vector which is the difference of a and b."
        return a+(-b)

    __eq__ = equal

    def __str__(v):
        "pretty-printing"
        D_list = sorted(v.D, key=repr)
        numdec = 3
        wd = dict([(k,(1+max(len(str(k)), len('{0:.{1}G}'.format(v[k], numdec))))) if isinstance(v[k], int) or isinstance(v[k], float) else (k,(1+max(len(str(k)), len(str(v[k]))))) for k in D_list])
        # w = 1+max([len(str(k)) for k in D_list]+[len('{0:.{1}G}'.format(value,numdec)) for value in v.f.values()])
        s1 = ''.join(['{0:>{1}}'.format(k,wd[k]) for k in D_list])
        s2 = ''.join(['{0:>{1}.{2}G}'.format(v[k],wd[k],numdec) if isinstance(v[k], int) or isinstance(v[k], float) else '{0:>{1}}'.format(v[k], wd[k]) for k in D_list])
        return "\n" + s1 + "\n" + '-'*sum(wd.values()) +"\n" + s2

    def __repr__(self):
        return "Vec(" + str(self.D) + "," + str(self.f) + ")"

    def copy(self):
        "Don't make a new copy of the domain D"
        return Vec(self.D, self.f.copy())
