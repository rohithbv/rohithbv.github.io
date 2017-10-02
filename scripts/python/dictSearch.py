class DictSearch(object):
   def wordBreak(self, s, wordDict):
      """
      :type s: str
      :type wordDict: List[str]
      :rtype: bool
      """
      flagList = [False for _ in range(len(s)+1)]
      flagList[0] = True
      for i in range(1, len(s)+1):
         for j in range(0, i):
            if flagList[j] and s[j:i] in wordDict:
               flagList[i] = True
               break
      return flagList[len(s)]

if __name__ == '__main__':
   myObj = DictSearch()
   s = 'aaaaaaa'
   wordDict = ['aaaa', 'aaa']
   output = myObj.wordBreak(s, wordDict)
   print('Input = {}'.format(s))
   print('Output = {}'.format(output))
