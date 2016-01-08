"""Reads in the csv file at 
https://gist.githubusercontent.com/ilanasegall/6dd2040657eb924171f9/raw/35ae4246ec93fc8b743835c76c8807a44460e81a/sample.csv and 
prints out the number of users in each operating system 
"""
#import the csv reader library and the url reader
import csv
import urllib
import collections

url = 'https://gist.githubusercontent.com/ilanasegall/6dd2040657eb924171f9/raw/35ae4246ec93fc8b743835c76c8807a44460e81a/sample.csv'
response = urllib.urlopen(url)
reader = csv.reader(response)
data = list(reader)
parsed_data = {}

for line in data[1:]:

	if parsed_data.has_key(line[1]):
		parsed_data[line[1]] += int(line[2])
	else:
		parsed_data[line[1]] = int(line[2])

print(collections.Counter(parsed_data).most_common(1))