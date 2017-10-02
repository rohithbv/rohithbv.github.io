import sys
class AtoiConverter(object):
    @staticmethod
    def myAtoi(str):
        """
        :type str: str
        :rtype: int
        """
        power = 0
        result = 0
        for i in range(len(str)-1, -1, -1):
            num = ord(str[i]) - ord("0")
            if num >= 0 and num < 10:
                result += num * (10**power)
                power += 1
        return result

def begin(input):
	 print AtoiConverter.myAtoi(input)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        begin(sys.argv[1])
