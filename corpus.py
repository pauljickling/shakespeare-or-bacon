from nltk import FreqDist, Text
from nltk.corpus import PlaintextCorpusReader

corpus_root = 'filter_text'
books = PlaintextCorpusReader(corpus_root, '.*')
#print(books.fileids())
text1 = books.words(fileids=['essays_and_wisdom_of_the_ancients.txt'])
text2 = books.words(fileids=['new_atlantis.txt'])
text3 = books.words(fileids=['novum_organum.txt'])
text4 = books.words(fileids=['of_gardens.txt'])
text5 = books.words(fileids=['shakespeare.txt'])
text6 = books.words(fileids=['the_advancement_of_learning.txt'])

fdist1 = FreqDist(text1)
fdist5 = FreqDist(text5)

shakespeare_list = fdist5.hapaxes()
bacon_list = fdist1.hapaxes()
shake_numless = []
bacon_numless = []

for i in bacon_list:
	if not i.isdigit():
		bacon_numless.append(i)

for i in shakespeare_list:
	if not i.isdigit():
		shake_numless.append(i)

shake_len = len(shake_numless)
bacon_len = len(bacon_numless)
total_len = shake_len + bacon_len

counter = 0
shared_list = []

for i in bacon_numless:
	if i in shake_numless:
		counter += 1
		shared_list.append(i)

print("Shared hapaxes: ", counter)
print("Shakespeare hapax list length: ", shake_len)
print("Bacon hapax list length: ", bacon_len)
print("Total hapax list length: ", total_len)