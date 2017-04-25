# networking-xml.py

import urllib
import xml.etree.ElementTree as ET 

url = raw_input("Enter Location: ")
print "Retrieving", url

filehandle = urllib.urlopen(url)
xml = filehandle.read()
print "Retrieved", len(xml), "characters"

root = ET.fromstring(xml)
counts = root.findall('.//count')
print 'Count:', len(counts)

total = 0
for count in counts:
	total = total + int(count.text)

print "Sum:", total