class Solution(object):
	def convert(self, s, numRows):
		"""
			:type s: str
			:type numRows: int
			:rtype: str
		"""
		i = 0
		returnStr = ""
		myList = list()
		newList = [[] for j in range(numRows)]
		while i < len(s):
			myList.append(s[i:i+numRows])
			myList.append(s[i+numRows:i+numRows+1])
			i += numRows+1
		for tok in myList:
			if len(tok) == 1:
				newList[numRows//2].append(tok)
			elif len(tok) <= numRows:
				for i in range(len(tok)):
					newList[i].append(tok[i:i+1])
		return ''.join(str(x) for _list in newList for x in _list)
			

if __name__ == '__main__':
	myObj = Solution()
	print myObj.convert("ABC", 2)
