# removes numbers from text
def remove_nums(text):
	new = text.lstrip().strip('0123456789')
	return new

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

shakespeare_set = set()

TEXTFILE = "src_text/shakespeare.txt"
with open(TEXTFILE) as file:
	for i, line in enumerate(file):
		if i > 300 and i < 400:
			new_line = remove_nums(line)
			shakespeare_set.add(new_line.rstrip())

print(shakespeare_set)