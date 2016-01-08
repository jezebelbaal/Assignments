# Takes in any amount of numbers and prints the sum of all of them

import sys
 
# Get the arguments list 
cmdargs = sys.argv

#sets a loop index
indice = len(cmdargs)

i = 1
total = 0

#loops all args
while i < indice:
	#print(cmdargs[i])
	total = total + int(cmdargs[i])
	i = i+1

print (total)