import csv
from collections import Counter

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

shakespeare_list = []
text_list = ["filter_text/essays_and_wisdom_of_the_ancients.txt", "filter_text/new_atlantis.txt", "filter_text/novum_organum.txt", "filter_text/of_gardens.txt", "filter_text/shakespeare.txt", "filter_text/the_advancement_of_learning.txt"]
bacon_list = []

def add_words(textfile, arr):
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
						arr.append(word.lower())

add_words(text_list[0], bacon_list)
add_words(text_list[1], bacon_list)
add_words(text_list[2], bacon_list)
add_words(text_list[3], bacon_list)
add_words(text_list[4], shakespeare_list)
add_words(text_list[5], bacon_list)

s_counter = Counter(shakespeare_list)
b_counter = Counter(bacon_list)

with open('filter_text/shakespeare_words.csv', 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(['word'])
	for i in shakespeare_list:
		csvwriter.writerow([i])

with open('filter_text/bacon_words.csv', 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(['word'])
	for i in bacon_list:
		csvwriter.writerow([i])

with open('filter_text/shakespeare_count.csv', 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(['word'] + ['frequency'])
	for k, v in s_counter.items():
		csvwriter.writerow([k] + [v])

with open('filter_text/bacon_count.csv', 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(['word'] + ['frequency'])
	for k, v  in b_counter.items():
		csvwriter.writerow([k] + [v])