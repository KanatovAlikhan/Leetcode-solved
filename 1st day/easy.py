#Given an integer x, return true if x is a palindrome, and false otherwise.
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        t=str(x)
        s=""
        length= len(t)-1
        for i in range(length,-1,-1):
            s+=t[i]
        if s==t:
            return True
        else:
            return False
'''
#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        inn = False
        for i in range(len(nums)):
            if target == nums[i]:
                inn = True
                return i
        if inn == False:
            if nums[length-1]>target:
                for i in range(len(nums)):
                    if nums[i]>=target:
                        return i 
            else:
                return length
'''
#You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
'''
class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans= 0 
        length = len(s)
        for i in range(len(s)):
            if i+1<length:
                ans+=abs(ord(s[i]) - ord(s[i+1]))
        return ans
'''