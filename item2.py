from nltk import FreqDist

def media(entrada):
    '''
    Essa função calcula a quantidade média de caracteres
    de cada palavra do texto dado como entrada.
    '''
    fdist = FreqDist(len(w) for w in entrada)
    somaTotal = 0
    for tam in fdist.most_common():
        somaTotal += tam[0] * tam[1]   
    
    resultadoMedia = somaTotal/fdist.N()
    return resultadoMedia

def LDS(entrada):
    '''
    Essa função calcula a variação léxica do texto de entrada.
    A variação léxica é a divisão da quantidade de palavras únicas pela 
    quantidade de palavras totais do texto.
    '''
    resultado = len(set(entrada))/len(entrada)
    return resultado