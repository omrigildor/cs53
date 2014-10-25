def my_filter(L, num): return [x for x in L if x % num != 0]

print(my_filter([1,2,3,4,5,7],2))

def my_lists(L):
    to_ret = []
    for num in L:
        if num == 0:
            to_ret.append([])
        else:
            new_L = []
            while num != 0:
                new_L.append(num)
                num = num - 1

            to_ret.append(new_L[::-1])

    return to_ret

print(my_lists([1,2,4]))

def my_function_composition(f,g): return {x:g.get(f.get(x)) for x in f}

print(my_function_composition({0:'a',1:'b'},{'a':'apple','b':'banana'}))

def mySum(L):
    sum = 0
    for num in L:
        sum = num + sum
    return sum

def myProduct(L):
    product = 1
    for num in L:
        product = product * num
    return product if L != [] else -1

def myMin(L):
    if L == []:
        return -1
    current = L[0]
    for num in L:
        if num < current:
            current = num
    return current

def myConcat(L):
    string = ""
    for s in L:
        string = string + s
    return string

def myUnion(L):
    s = {}
    for set in L:
        s = s & set
    return s

#1.7.9
# 1 - 0
# 2 - 0
# 3 - -1
# 4 - empty string ""
# 5 - empty set {}
# The intersection of an empty list of sets is the empty set



act = {'a':2, 'b':3}
fed = {'a':1, 'b':4}
print({x:(act[x] + fed[x]) for x in act})
