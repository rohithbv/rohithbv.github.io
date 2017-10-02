class StringOperations(object):
   @staticmethod
   def reverseString(s):
      myList = list(s)
      left = 0
      right = len(s) - 1
      while left < right:
         myList[left], myList[right] = myList[right], myList[left]
         left += 1
         right -= 1
      return ''.join(myList)

   @staticmethod
   def reverseWordsInString(s):
      result = []
      subStrStart = 0
      for i in range(len(s)):
         if s[i] == ' ':
            result.append(StringOperations.reverseString(s[subStrStart:i]))
            subStrStart = i
            result.append(' ')
      result.append(StringOperations.reverseString(s[subStrStart:len(s)]))
      return ''.join(result)

   @staticmethod
   def isPalindrome(s):
      left = 0
      right = len(s) - 1
      while left < right:
         if s[left] != s[right]:
            print('{} is not a palindrome'.format(s))
            return
         left += 1
         right -= 1
      print('"{}" is a palindrome'.format(s))

   @staticmethod
   def areStringsAnagrams(s1, s2):
      myDict = {}
      for i in s1:
         if myDict.has_key(i):
            myDict[i] += 1
         else:
            myDict[i] = 1
      for i in s2:
         if myDict.has_key(i):
            myDict[i] -= 1
         else:
            print('"{}" and "{}" are not anagrams'.format(s1, s2))
            return
      for val in myDict.itervalues():
         if val != 0:
            print('"{}" and "{}" are not anagrams'.format(s1, s2))
            return
      print('"{}" and "{}" are anagrams'.format(s1, s2))

   @staticmethod
   def stringPermutations(s):
      result = None
      if s:
         if len(s) > 0:
            result = StringOperations.performPermutations('', s)
      return result

   @staticmethod
   def performPermutations(perm, word):
      result = []
      if len(word) == 0:
         result.append(''.join([perm, word]))
      else:
         for i in range(len(word)):
            result.append(StringOperations.performPermutations(perm + word[i], word[0:i]+word[i+1:len(word)]))
      return result

   @staticmethod
   def removeDuplicateChars(s):
      result = []
      myDict = {}
      for _ in s:
         if _ not in result:
            result.append(_)
      return ''.join(result)

   @staticmethod
   def isStringShuffled(s1, s2, s3):
      if len(s1) == len(s2) == len(s3) == 0:
         return True
      if (len(s1) == len(s2) == 0) and len(s3) != 0:
         return False
      if (len(s1) != 0 or len(s2) != 0) and len(s3) == 0:
         return False

      s1Val = s1[0] if len(s1) > 0 else None
      s2Val = s2[0] if len(s2) > 0 else None
      s3Val = s3[0] if len(s3) > 0 else None

      if s1Val == s3Val:
         result = StringOperations.isStringShuffled(s1[1:], s2, s3[1:])
      elif s2Val == s3Val:
         result = StringOperations.isStringShuffled(s1, s2[1:], s3[1:])
      else:
         result = False
      return result

   @staticmethod
   def areStringsSubStrings(str1, str2):
      result = -1
      cFlag = False
      j = 0
      if (not str1) or (not str2): return False
      if len(str1) > len(str2):
         s1 = str1
         s2 = str2
      else:
         s1 = str2
         s2 = str1
      for i in range(len(s1)):
         if not cFlag:
            if s1[i] == s2[j]:
               cFlag = True
               j += 1
               result = i
               if j < len(s2): continue
               else: return result
         else:
            if s1[i] == s2[j]:
               j += 1
               if j < len(s2): continue
               else: return result
            else:
               cFlag = False
               result = -1
               j = 0
      if len(s1[result:]) == len(s2): result = True
      else: result = -1
      return result
     

if __name__ == '__main__':
#   input = 'racecar'
#   output = StringOperations.reverseString(input)
#   print('Input = {}'.format(input))
#   print('Output = {}'.format(output))
#   print '#####'
#   StringOperations.isPalindrome(input)
#   StringOperations.areStringsAnagrams('cat', 'acts')
#   print '#####'
#   input = 'xyz'
#   output = StringOperations.stringPermutations(input)
#   print('Input = {}'.format(input))
#   print('Output = {}'.format(output))
#   print '#####'
#   input = 'hello world'
#   output = StringOperations.reverseWordsInString(input)
#   print('Input = {}'.format(input))
#   print('Output = {}'.format(output))
#   print '#####'
#   input = 'hello world'
#   output = StringOperations.removeDuplicateChars(input)
#   print('Input = {}'.format(input))
#   print('Output = {}'.format(output))
#   print '#####'
#   res = StringOperations.isStringShuffled('abc', 'def', 'dabecf')
#   print res
   print StringOperations.areStringsSubStrings('dab', 'abcd')


   pass
