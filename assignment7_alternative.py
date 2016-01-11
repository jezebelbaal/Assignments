#Reads in a word file and prints it out in uppercase
import fileinput as file_io
import operator as op

inputfile = file_io.input()

#I know it's way better to use regex, but I quite failed :(

parsed_data = {}

for line in inputfile:

	line = line.replace("\n", "")
	line = line.replace(".", "")
	line = line.replace(",", "")
	line = line.replace("!", "")
	line = line.lower();

	words = line.split(" ")
	

	for word in words:
		if word=="":
				continue
		if word in parsed_data:
			
			parsed_data[word] = parsed_data[word] +1

		else:
			parsed_data[word] = 1

most_common = max(parsed_data.iteritems(), key=op.itemgetter(1))[0]

print "Word counts: /n"
print parsed_data
print  "Most common word: " + most_common + ": " + str(parsed_data[most_common])


