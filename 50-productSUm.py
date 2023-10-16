def subtractProductAndSum(n):
        """
        :type n: int
        :rtype: int
        """

        pro,sum=1,0

        while n!=0:
           r=n%10
           pro=pro*r
           sum=sum+r
           n=int(n/10)
        
        return pro-sum

ans=subtractProductAndSum(234)
print(ans)

"""
Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21

"""
