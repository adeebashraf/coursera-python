file = open('mbox-short.txt')

time_count = dict()

for line in file:
	if line.startswith('From '):
		words = line.split()
		time = words[5].split(':')
		time_count[time[0]] = time_count.get(time[0], 0) + 1
        
time_count_list = sorted(time_count.items())

for key, value in time_count_list:
	print key, value