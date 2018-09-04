from nltk.book import *

def hapaxes():
    fdist = FreqDist(text1)
    return fdist.hapaxes()

def collocations():
    text1.collocations()

def maisFrequentes(qtMaisFrequentes):
    fdist = FreqDist(text1)
    return fdist.most_common(qtMaisFrequentes)