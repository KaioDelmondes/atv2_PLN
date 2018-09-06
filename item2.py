from nltk.book import FreqDist

def media(entrada):
    fdist = FreqDist(len(w) for w in entrada)
    somaTotal = 0
    for tam in fdist.most_common():
        somaTotal += tam[0] * tam[1]   
    
    resultadoMedia = somaTotal/fdist.N()
    return resultadoMedia

def LDS(entrada):
    resultado = len(entrada)/len(set(entrada))
    return resultado