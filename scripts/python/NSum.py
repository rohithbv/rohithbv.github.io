class NSum(object):
	@staticmethod
	def findFourSum(nums, sum):
		result = list()
		visited = list()
		for i in range(len(nums)):
			visited.append(i)
			output = NSum.findThreeSum([nums[j] for j in range(len(nums)) if (j not in visited)], sum-nums[i])
			for listId in range(len(output)): result.append([nums[i]] + output[listId])
		return result

	@staticmethod
	def findThreeSum(nums, sum):
		result = list()
		visited = list()
		for i in range(len(nums)):
			visited.append(i)
			output = NSum.findTwoSum([nums[j] for j in range(len(nums)) if (j not in visited)], sum-nums[i])
			for listId in range(len(output)): result.append([nums[i]] + output[listId])
		return result

	@staticmethod
	def findTwoSum(nums, sum):
		myMap = dict()
		result = list()
		for i in nums:
			if myMap.has_key(i):
				result.append([myMap[i], i])
			myMap[sum-i] = i
		return result


if __name__ == '__main__':
	input = [1, 1, 0, 2, 3, 4, 5]
#	input = [-1, 0, 1, 2, -1, -4]
	print("Input list = %s" % input)
	sum = 6
	output = NSum.findTwoSum(input, sum)
	print("Two Sum result for sum=%d is: %s" % (sum, output))
	output = NSum.findThreeSum(input, sum)
	print("Three Sum result for sum=%d is: %s" % (sum, output))
	output = NSum.findFourSum(input, sum)
	print("Four Sum result for sum=%d is: %s" % (sum, output))
