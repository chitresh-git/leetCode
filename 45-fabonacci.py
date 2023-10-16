def fib(n):
        """
        :type n: int
        :rtype: int
        """
        n=n-1

        a,b=0,1
        print(a)
        print(b)

        for i in range(n):
                b,a=b+a,b
        return b


ans=fib(4)
print(ans)

"""
Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
"""