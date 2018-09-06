import nltk
from nltk.corpus import PlaintextCorpusReader 
from nltk.corpus import stopwords

stopWords = stopwords.words('portuguese')
loc = "./data_corpus/"
corpus = PlaintextCorpusReader(loc, '.*\.txt')

cfd = nltk.ConditionalFreqDist(
	(gen, pal.lower())
	for gen in corpus.fileids()
	for pal in corpus.words(fileids=gen) if pal.lower() not in stopWords and pal.isalpha()
)
cfd.plot(title="Exibindo a Frequncia das palavras de sites governamentais",conditions=['sites_governametais.txt'])
cfd.tabulate()
