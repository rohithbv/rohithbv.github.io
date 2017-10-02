class DictSearch(object):
   def wordBreak(self, s, wordDict):
      """
      :type s: str
      :type wordDict: List[str]
      :rtype: bool
      """
      endIdx = len(s)
      length = 0
      for i in range(endIdx-1, -1, -1):
         if s[i:endIdx] in wordDict:
            length += endIdx - i
            print str(s[i:endIdx])
            wordDict.remove(s[i:endIdx])
            endIdx = i
      print length
      if len(s) == length: return True
      else: return False

if __name__ == '__main__':
   myObj = DictSearch()
   s = 'aaaaaaa'
   wordDict = ['aaaa', 'aaa']
   output = myObj.wordBreak(s, wordDict)
   print('Input = {}'.format(s))
   print('Output = {}'.format(output))
