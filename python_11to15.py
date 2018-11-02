class Solution11:
	def maxArea(self, height):
		l, r = 0, len(height) - 1
		max_area = 0
		while l < r:
			curr_area = min(height[l], height[r]) * (r - l)
			max_area = max(curr_area, max_area)

			if height[l] > height[r]:
				r -= 1
			else:
				l += 1

		return max_area



########################################################################
#solution 12:

class Solution12:
	r = {
        # value is an array of strings for each key in
        # the ones, tens, hundreds, and thousands places
        # up to 3000 (since given max is 3999)
        1: ['I', 'X', 'C', 'M'],
        2: ['II', 'XX', 'CC', 'MM'],
        3: ['III', 'XXX', 'CCC', 'MMM'],
        4: ['IV', 'XL', 'CD'],
        5: ['V', 'L', 'D'],
        6: ['VI', 'LX', 'DC'],
        7: ['VII', 'LXX', 'DCC'],
        8: ['VIII', 'LXXX', 'DCCC'],
        9: ['IX', 'XC', 'CM']
    }

	def intToRoman(self, num):
		"""
        :type num: int
        :rtype: str
        """
		ret = ""
		for i in range(len(str(num))):
			digit = (num // (10 ** i)) % 10
			if digit > 0:
				ret = self.r[digit][i] + ret
		return ret

################################################################################
#solution13:

class Solution13:
	def romanToInt(self, s):
		num = 0
		dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': -2, 'IX': -2, 'XL': -20,
				'XC': -20, 'CD': -200, 'CM': -200}
		for key in dict:
			num = num + s.count(key) * dict[key]
		return num




################################################################################
#solution15: 3sum

nums = [-1, 0, 1, 2, -1, -4]


class Solution:
	def threeSum(self, nums):

		nums.sort()
		A = []
		nums1 = nums
		for i in nums:
			numsi = [x for x in nums if x != i]
			for j in numsi:
				numsi.remove(j)
				if (-i - j) in numsi:
					a = [i, j, (-i - j)]
					a.sort()
					A.append(a)

			nums = nums1
		A = sorted(A)
		dedup = [A[i] for i in range(len(A)) if i == 0 or A[i] != A[i - 1]]

		return dedup
