def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        1295
        """

        res=[x for x in nums if (x>=10**1 and x<10**2) or (x>=10**3 and x<10**4) or (x==10**5)]

        return len(res)

"""
Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
"""
