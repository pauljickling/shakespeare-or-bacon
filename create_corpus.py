from nltk.corpus import PlaintextCorpusReader
corpus_root = 'filter_text'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
