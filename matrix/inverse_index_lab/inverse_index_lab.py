from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randomint(0,len(review_options)-1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    docDic = {k:v for (k,v) in enumerate(strlist)}
    #print(docDic)
    wholeString = ""
    for item in strlist:
        wholeString += " "
        wholeString += item
    allWords = set(wholeString.split())
    
    inverseDic = {}
    for word in allWords:
        if not word in inverseDic:
            inverseDic[word] = []
        for (no,doc) in docDic.items():
            if word in doc.split():
                inverseDic[word].append(no)
    #print(inverseDic)
    return inverseDic

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """

    noList = [inverseIndex[word] for word in query]
    
    return set(sum(noList,[]))

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    noList = [inverseIndex[word] for word in query]
    if len(noList) != 0:
        retSet = set(noList[0])
        for aList in noList:
            retSet = retSet & set(aList)
        return retSet
    else:
        return Null