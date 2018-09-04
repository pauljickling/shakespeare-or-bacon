TEXTFILE = "src_text/shakespeare.txt"
text = open(TEXTFILE, 'r')
shakespeare = text.read()
print(shakespeare)