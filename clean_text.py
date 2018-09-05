def clean(text):
	new = text.lstrip().strip('0123456789')
	return new

shakespeare_set = set()

TEXTFILE = "src_text/shakespeare.txt"
with open(TEXTFILE) as file:
	for i, line in enumerate(file):
		if i > 300 and i < 400:
			new_line = clean(line)
			shakespeare_set.add(new_line.rstrip())

print(shakespeare_set)