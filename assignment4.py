# Takes in any amount of numbers and prints their sum, product, the first element in the list, 
#and the last element in the list. Use functions for each of these tasks


import sys
#function that sums all arguments given

def sumargs(argslist):
	 return(sum(argslist))

def multiplyargs(argslist):
	product = 1
	for x in argslist:
		product=product*x
	return product

def firstnumber(argslist):
	return str(argslist[0])

def lastnumber(argslist):
	return str(argslist[len(argslist)-1])

# declare an arguments list 
cmdargs = []

#sets a loop index
index = len(sys.argv)

i = 1
total = 0

#loops all args converting to int

while i < index:
	cmdargs.append(int(sys.argv[i]))
	i = i+1

print "Sum of numbers:" + str(sumargs(cmdargs))

print "Product of the numbers:" + str((multiplyargs(cmdargs)))

print  "First number:" + firstnumber(cmdargs)

print "Last number:" + lastnumber(cmdargs)
