#16:3sumleast
class Solution:
	def threeSumClosest(self, num, target):
		num.sort()
		result = num[0] + num[1] + num[2]
		for i in range(len(num) - 2):
			j, k = i + 1, len(num) - 1
			while j < k:
				sum = num[i] + num[j] + num[k]
				if sum == target:
					return sum

				if abs(sum - target) < abs(result - target):
					result = sum

				if sum < target:
					j += 1
				elif sum > target:
					k -= 1

		return result


#17:Letter Combinations of a Phone Number
class Solution:
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""

		if len(digits) == 0:
			return []
		d = {'2': 'abc',
			 '3': 'def',
			 '4': 'ghi',
			 '5': 'jkl',
			 '6': 'mno',
			 '7': 'pqrs',
			 '8': 'tuv',
			 '9': 'wxyz'}
		acc = [e for e in d[digits[0]]]  # Avoiding a always empty list in for loop
		for digit in digits[1:]:
			acc = [w1 + w2 for w1 in acc for w2 in d[digit]]
		return acc