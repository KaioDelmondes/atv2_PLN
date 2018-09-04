from nltk.book import *

def media():
    fdist = FreqDist(len(w) for w in text1)
    somaTotal = 0
    for tam in fdist.most_common():
        somaTotal += tam[0] * tam[1]   
    
    resultadoMedia = somaTotal/fdist.N()
    return resultadoMedia