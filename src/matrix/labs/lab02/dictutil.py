# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [dct[x] for x in keylist]

def list2dict(L, keylist): return {keylist[x]:L[x] for x in range(len(keylist))}

def listrange2dict(L): return {x:L[x] for x in range(len(L))}

def makeInverseIndex(strlist):
    d = {}
    for i, article in enumerate(strlist):
        for word in article.split(" "):
            if word in d:
                d[word].append(i)
            else:
                d[word] = [i]

    return d

print(makeInverseIndex(["mary had a little lamb", "whose fleece was white as snow", "mary had a little white snow lamb"]))

i_i = makeInverseIndex(["mary had a little lamb", "whose fleece was white as snow", "mary had a little white snow lamb"])


def orSearch(inverseIndex, query):
    d = set()
    for word in query.split(' '):
        if word in inverseIndex:
            for i in inverseIndex[word]:
                d.add(i)

    return d

print(orSearch(i_i, "mary snow little lamb"))

def andSearch(inverseIndex, query):
    d = set()
    first = True
    for word in query.split(" "):
        if word in inverseIndex:
            if first:
                for i in inverseIndex[word]:
                    d.add(i)
                    first = False
            else:
                for i in inverseIndex[word]:
                    if i in d:
                        d.add(i)


    return d


print(andSearch(i_i,("was white")))