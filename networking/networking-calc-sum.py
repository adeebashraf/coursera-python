import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url)

#print html.read()

soup = BeautifulSoup(html)

#print soup

span_tags = soup('span')
count = 0
total = 0

for span in span_tags:
	total = total + int(span.contents[0])
	count = count + 1

print 'Count', count
print 'Sum', total
	