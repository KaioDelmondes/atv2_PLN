from nltk import FreqDist


def hapaxes(entrada):
    '''
    Hapaxes são palavras que ocorrem apenas uma vez no texto.
    Essa função é responsável por retornar uma lista dessas palavras.
    '''
    fdist = FreqDist(entrada)
    return fdist.hapaxes()

def collocations(entrada):
    '''
    Collocations são duplas com palavras que aparecem raras vezes no texto,
    mas quando ocorrem, na maioria das vezes formam uma dupla.
    Essa função retorna as collocations do texto de entrada.
    '''
    entrada.collocations()

def maisFrequentes(entrada,qtMaisFrequentes):
    '''
    Essa função retorna as palavras mais comuns do texto.
    O parâmetro "qtMaisFrequestes" limita a quantidade de palavras a serem retornadas.
    '''
    fdist = FreqDist(entrada)
    return fdist.most_common(qtMaisFrequentes)