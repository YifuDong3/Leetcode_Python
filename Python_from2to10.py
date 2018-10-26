#!/usr/bin/env python3
# -*- coding: utf-8 -*-




################################################
#a simple test .
class ListNode2:

	def __init__(self, x):
		self.val = x
		self.next = None
		self.add=self.val*5
	def addcount(self):
		print "begin"
		t=self.add*4
		return t

a=ListNode2(4)


print a.add
print a.addcount()

##################################################
##leetcode : problem3 ---- longest substring without repeating characters


class Solution:
	def __init__(self,s):
		"""
		:type s: str
		:rtype: int
		"""
		self.s = s

	def substring(self):
		if len(self.s) <= 1:
			return len(self.s)
		list1 = []
		for i in range(len(self.s)):
			for j in range(len(self.s) - 1):
				if self.s[i - 1] == self.s[j]:
					list1.append(j - i + 1)
		return max(list1)

c=raw_input("Please input a string: ")  ### input and output. please pay attention to the python version,
# here we use python2.7 so we use raw_input

a = Solution(c)
print(a.substring())



#################################################################
# leetcode: problem4 ---- Median of two sorted arrays.

class Solution4:
	def findMedianSortedArray(self,nums1,nums2):
		self.nums1=nums1
		self.nums2=nums2

		listnum = self.nums1 + self.nums2
		listnum.sort()
		if len(listnum) % 2 == 0:
			median = (listnum[int(len(listnum) / 2) - 1] + listnum[int(len(listnum) / 2)]) / 2
		elif len(listnum) % 2 == 1:
			median = listnum[int((len(listnum) + 1) / 2 - 1)]
		return median

num1=[1,2,5]
num2=[3,5,4]
a4=Solution4()
a4.findMedianSortedArray(num1,num2)



######################################################################
#leetcode: problem5---- Longest Palindromic Substring.




