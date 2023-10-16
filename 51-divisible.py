def sumOfMultiples(n):
        """
        :type n: int
        :rtype: int
        """

 
        sum=0

        for e in range(1,n+1):
                if e%3==0 or e%5==0 or e%7==0:
                        print(e)
                        sum=sum+e
        
        return sum

ans=sumOfMultiples(7)
print(ans)

"""
Example 1:

Input: n = 7
Output: 21
Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.
Example 2:

Input: n = 10
Output: 40
Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40.
Example 3:

Input: n = 9
Output: 30
Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9. The sum of these numbers is 30.
"""

                        