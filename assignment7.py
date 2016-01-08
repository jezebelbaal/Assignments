#Reads in a word file and prints it out in uppercase
import collections

textfile = open('E:/outreachy/Assignments/poem.txt', 'r')

text = textfile.read()


#I know it's way better to use regex, but I quite failed :(
text = text.replace("\n", " ")
text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("!", "")
text = text.lower();

words = text.split(" ")

print("The number of each word:")
print(collections.Counter(words))


print (collections.Counter(words).most_common(3))
