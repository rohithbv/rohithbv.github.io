def swapListElements(myList, i, j):
	temp = myList[i]
	myList[i] = myList[j]
	myList[j] = temp

def bubbleSort(input):
	myList = input[:]
	sorted = False
	while not sorted:
		sorted = True
		for i in range(len(myList) - 1):
			if myList[i] > myList[i + 1]:
				swapListElements(myList, i, i+1)
				sorted = False
	return myList


if __name__ == '__main__':
	myList = [4, 6, 1, 0, 9, 5]
	result = bubbleSort(myList)
	print "Input list = %s" % myList
	print "Result after bubble sort = %s" % result
