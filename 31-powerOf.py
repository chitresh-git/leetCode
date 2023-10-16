def isPowerOfTwo(n):
        """
        :type n: int
        :rtype: bool
        """

        count=0
        m=n

        while n!=1:
            n=int(n/2)
            # print(n)
            count+=1
        if m==2**count:
                  return count 
        else:
                  return False
        
        

ans=isPowerOfTwo(3)
print(ans)

"""
Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
"""