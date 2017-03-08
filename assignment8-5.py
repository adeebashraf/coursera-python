filename = raw_input('Enter file name: ')
fhandle = open(filename)
count = 0
for line in fhandle:
	if not line.startswith('From '): continue
	line_words = line.split()
	print line_words[1]
	count = count + 1

print "There were", count, "lines in the file with From as the first word"
