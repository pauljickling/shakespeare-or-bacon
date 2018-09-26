from nltk import FreqDist, Text
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'filter_text'
books = PlaintextCorpusReader(corpus_root, '.*')
print(len(books.fileids()))
text1 = books.words(fileids=['essays_and_wisdom_of_the_ancients.txt'])
fdist1 = FreqDist(text1)
print(fdist1)