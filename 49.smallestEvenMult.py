def smallestEvenMultiple(n):
        """
        :type n: int
        :rtype: int
        """

        if n%2==0:
            return n

        else :
            return n*2
        

ans=smallestEvenMultiple(15)
print(ans)

"""
Example 1:

Input: n = 5
Output: 10
Explanation: The smallest multiple of both 5 and 2 is 10.
Example 2:

Input: n = 6
Output: 6
Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.
"""
        
