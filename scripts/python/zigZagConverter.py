class ZigZagConverter(object):
   def convert(self, s, numRows):
      """
      :type s: str
      :type numRows: int
      :rtype: str
      """
      if len(s) < numRows:
         return s
      i = 0
      resultStr = ''
      newList = [[] for j in range(numRows)]
      while i < len(s):
         for idx in range(numRows):
            if i < len(s):
               newList[idx].append(s[i])
               i += 1
         for idx in range(numRows-2, 0, -1):
            if i < len(s):
               newList[idx].append(s[i])
               i += 1
      for _ in newList: resultStr += ''.join(_)
      return resultStr

if __name__ == '__main__':
   myObj = ZigZagConverter()
   input = 'PAYPALISHIRING'
   numRows = 3
   output = myObj.convert(input, numRows)
   print('Input string = {}'.format(input))
   print('Output string = {}'.format(output))
