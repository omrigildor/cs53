# version code a3133383da20
# Please fill out this stencil and submit using the provided submission script.

from random import randint



## 1: (Task 0.6.2) Movie Review
## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    return ["See it!", "A gem!", "Ideological claptrap"][randint(0,2)]



## 2: (Task 0.6.6) Make Inverse Index
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.
    Distinguish between an occurence of a string (e.g. "use") in the document as a word
    (surrounded by spaces), and an occurence of the string as a substring of a word (e.g. "because").
    Only the former should be represented in the inverse index.
    Feel free to use a loop instead of a comprehension.

    Example:
    >>> makeInverseIndex(['hello world','hello','hello cat','hellolot of cats'])
    {'hello': {0, 1, 2}, 'cat': {2}, 'of': {3}, 'world': {0}, 'cats': {3}, 'hellolot': {3}}
    """
    d = {}
    for i, article in enumerate(strlist):
        for word in article.split():
            if word in d:
                d[word].add(i)
            else:
                d[word] = {i}

    return d

## 3: (Task 0.6.7) Or Search
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    Feel free to use a loop instead of a comprehension.
    
    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> orSearch(idx, ['Bach','the'])
    {0, 2, 3, 4, 5}
    >>> orSearch(idx, ['Johann', 'Carl'])
    {0, 2, 3, 4, 5}
    """
    d = set()
    for word in query:
        if word in inverseIndex:
            for i in inverseIndex[word]:
                d.add(i)

    return d



## 4: (Task 0.6.8) And Search
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    Feel free to use a loop instead of a comprehension.

    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> andSearch(idx, ['Johann', 'the'])
    {2, 3}
    >>> andSearch(idx, ['Johann', 'Bach'])
    {0, 4}
    """
    d = set()
    first = True
    for word in query:
        if word in inverseIndex:
            if first:
                for i in inverseIndex[word]:
                    d.add(i)
                    first = False
            else:
                d = d & inverseIndex[word]


    return d


#
# i_i = makeInverseIndex(["mary had a little lamb", "whose fleece was white as snow", "mary had a little white snow lamb"])
#
#
# print (i_i)
#
# print(orSearch(i_i, ["mary","snow","little","lamb"]))
#
# print(andSearch(i_i, ["mary","snow","little","lamb"]))
