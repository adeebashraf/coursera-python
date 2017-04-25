import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
count = int(count)
position = raw_input('Enter position: ')
position = int(position)
loop_counter = 0
print "Retrieving: ", url

while (loop_counter < count):
	html_text = urllib.urlopen(url).read()
	html = BeautifulSoup(html_text)
	a_tags = html('a')
	
	url = a_tags[position-1].get('href', None)
	print "Retrieving: ", url
	loop_counter = loop_counter + 1
	