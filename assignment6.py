#Reads in a word file and prints it out in uppercase
textfile = open('E:/outreachy/Assignments/poem.txt', 'r')

text = textfile.readlines()

print(text[0])

print(text[-1])