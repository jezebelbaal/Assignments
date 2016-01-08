#Reads in a word file and prints it out in uppercase
textfile = open('E:/outreachy/Assignments/poem.txt', 'r')

text = textfile.readlines()

for line in text:
	print(line.upper())