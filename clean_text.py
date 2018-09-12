import re

# parses a string into separates words, and appends them to a returned list
def parse_words(str):
	str = str + ' '
	word = ''
	word_list = []
	for i in str:
		if i == ' ':
			word_list.append(word)
			word = ''
		else:
			word = word + i
	return word_list

word_list = []

TEXTFILE = "src_text/shakespeare.txt"
with open(TEXTFILE) as file:
	for i, line in enumerate(file):
		if i > 3000 and i < 3400:
			new_line = line.lstrip().strip('0123456789')
			new_line = new_line.rstrip()
			new_line = new_line.replace('.', ' ')
			new_line = new_line.replace(',', ' ')
			new_line = new_line.replace('?', ' ')
			new_line = new_line.replace('!', ' ')
			new_line = new_line.replace(';', ' ')
			new_line = new_line.replace(':', ' ')
			parsed = parse_words(new_line)
			for word in parsed:
				word_list.append(word)

print("First word list: ", word_list)

for i in word_list:
	if i.isupper():
		word_list.remove(i)

print("Second word list: ", word_list)