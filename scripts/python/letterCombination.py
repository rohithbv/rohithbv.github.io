from collections import deque

class LetterCombinations(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		myQueue = deque()
		if len(digits) == 0:
			return list(myQueue)
		myQueue.append("")
		myMap = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
		for i in range(len(digits)):
			curDigit = int(digits[i])
			while len(myQueue[0]) == i:
				temp = myQueue.popleft()
				for j in myMap[curDigit]:
					myQueue.append(temp+j)
		return list(myQueue)

if __name__ == '__main__':
	myObj = LetterCombinations()
	input = "236"
	output = myObj.letterCombinations(input)
	print("Phone combination for %s = %s" % (input, output))
