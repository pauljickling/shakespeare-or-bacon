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
text_list = ["filter_text/essays_and_wisdom_of_the_ancients.txt", "filter_text/new_atlantis.txt", "filter_text/novum_organum.txt", "filter_text/of_gardens.txt", "filter_text/shakespeare.txt", "filter_text/the_advancement_of_learning.txt"]
bacon_list = []

def add_words(textfile):
	with open(textfile) as file:
		for i, line in enumerate(file):
			new_line = line.lstrip().strip('0123456789')
			new_line = new_line.rstrip()
			new_line = new_line.replace('.', ' ')
			new_line = new_line.replace(',', ' ')
			new_line = new_line.replace('?', ' ')
			new_line = new_line.replace('!', ' ')
			new_line = new_line.replace(';', ' ')
			new_line = new_line.replace(':', ' ')
			new_line = new_line.replace('"', ' ')
			parsed = parse_words(new_line)
			for word in parsed:
				if word.isupper() == False:
					if word != '':
						bacon_list.append(word)

add_words(text_list[0])
add_words(text_list[1])
add_words(text_list[2])
add_words(text_list[3])
add_words(text_list[5])


with open('filter_text/bacon_word_list.txt', 'w') as file:
	file.write('[')
	for i in bacon_list:
		file.write(i.lower() + ", ")
	file.write(']')