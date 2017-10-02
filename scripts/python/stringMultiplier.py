class StringMultiplier(object):
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		result = carry = product = 0
		for i in range(len(num1)-1, -1, -1):
			power = len(num1) - 1 - i
			for j in range(len(num2)-1, -1, -1):
				val1 = int(num1[i])
				val2 = int(num2[j])
				product = (val1 * val2) + carry
				if j != 0:
					result += (product%10) * (10 ** power)
					carry = 0 if product < 10 else (product//10)
				else:
					result += product * (10 ** power)
					carry = 0
				power += 1
				result += carry * (10**power)
		return str(result)
