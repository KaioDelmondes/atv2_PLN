import nltk
from nltk import FreqDist
from nltk.corpus import PlaintextCorpusReader 

# O Corpus é criado através do PlaintextCorpusReader, os métodos fileids()
# e words() são referentes ao corpus e suas aplicações.

# para usar o corpus em outros arquivos basta copiar as linhas de codigo [10 - 13]
# o `loc` é o path para o data_corpus no pc

loc = input("Qual o caminho do data_corpus no seu pc? (/SEU_PATH/data_corpus/)")
corpus = PlaintextCorpusReader(loc, '.*\.txt') 
corpus.fileids()
corpus.words()

print("\n" + str(FreqDist(corpus.words()).most_common(50)))