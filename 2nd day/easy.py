#Write a function that reverses a string. The input string is given as an array of characters s.
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        my_list=list()
        for i in s[::-1]:
            my_list.append(i)
        for i in range(len(my_list)):
            s[i]=my_list[i]
'''
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = 0 
        my_list=list()
        c=0
        for i in range(len(nums)):
            c+=1
            for j in range(c,len(nums)):
                sum = nums[i]+nums[j]
                if sum == target:
                    my_list.append(i)
                    my_list.append(j)
        return my_list
'''
#Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
'''
import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            return int(math.sqrt(x))
'''
