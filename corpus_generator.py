from nltk.corpus.reader.tagged import TaggedCorpusReader 

loc = '/data_corpus/'

corpus = PlaintextCorpusReader(loc, '.*\.txt')
corpus.fileids()
corpus.words()
corpus.sents()
corpus.tagged_words()