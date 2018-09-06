import nltk
from nltk import FreqDist
from nltk.corpus import PlaintextCorpusReader 

loc = input("Qual o caminho do data_corpus no seu pc? (/SEU_PATH/data_corpus/)")

# O Corpus é criado através do PlaintextCorpusReader, os métodos fileids()
# e words() são referentes ao corpus e suas aplicações.

corpus = PlaintextCorpusReader(loc, '.*\.txt')