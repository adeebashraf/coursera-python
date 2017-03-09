name = raw_input('Enter filename: ')
if(len(name) < 1):
	name = 'mbox-short.txt'

file = open(name)

words = list()
senders = list()

for line in file:
	if not line.startswith('From '): continue
	words = line.split()
	senders.append(words[1])

committer = dict()
for sender in senders:
	committer[sender] = committer.get(sender, 0) + 1


largest_email = None
largest_count = None
for email, count in committer.items():
	if largest_count == None or largest_count < count:
		largest_count = count
		largest_email = email

print largest_email, largest_count