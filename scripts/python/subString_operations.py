class SubStringOperations(object):
   @staticmethod
   def findShortestNonRepeatingSubString(s):
      subStrStart = 0
      resultStr = '                                         '
      myMap = {}
      for i in range(len(s)):
         if s[i] in myMap:
            resultStr = s[subStrStart:i] if len(s[subStrStart:i]) < len(resultStr) else resultStr
            subStrStart = i
         myMap[s[i]] = i
      resultStr = s[subStrStart:] if len(s[subStrStart:]) < len(resultStr) else resultStr
      return resultStr

   @staticmethod
   def findLongestNonRepeatingSubString(s):
      subStrStart = 0
      resultStr = ''
      myMap = {}
      for i in range(len(s)):
         if s[i] in myMap:
            resultStr = s[subStrStart:i] if len(s[subStrStart:i]) > len(resultStr) else resultStr
            subStrStart = i
         myMap[s[i]] = i
      resultStr = s[subStrStart:] if len(s[subStrStart:]) > len(resultStr) else resultStr
      return resultStr


if __name__ == '__main__':
   input = 'abcaabbcc'
   output = SubStringOperations.findShortestNonRepeatingSubString(input)
   print('Input = {}'.format(input))
   print('Output = {}'.format(output))
