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
headers = reader.next()
columns = {}
for h in headers:
	columns[h] = []

for row in reader:
	for h, v in zip(headers, row):
		columns[h].append(v)

print(collections.Counter(columns['os']).most_common(1))


