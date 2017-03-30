import re

fhandle = open('regex_sum_362824.txt')

file_text = fhandle.read()
numbers_list = re.findall('[0-9]+', file_text)

total = 0

for number in numbers_list:
    total = total + int(number)

print total
