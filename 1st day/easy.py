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
