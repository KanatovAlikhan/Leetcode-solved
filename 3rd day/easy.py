#Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
'''
class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.lower()
'''
#You are given an integer array nums with the following properties:
'''
nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.
'''
'''
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter=list()
        for i in range(10**4):
            counter.append(0)
        for i in nums:
            counter[i]+=1
        c=0
        for i in counter:
            if i<2:
                c+=1
            else:
                return c
'''
#Given an integer n, return true if it is a power of two. Otherwise, return false.
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans=False
        for i in range(0,40):
            if 2**i==n:
                ans=True
        return ans
        
'''