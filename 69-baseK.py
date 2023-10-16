def sumBase(n, k):
        # FAILED
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        

        if k==2:
                n=bin(n)
                n=int(n[2:])
                
        else:
          base=int(n/k)
          remains=n-(base*k)
          n=(base*10)+remains
        
        print(n)

        sum=0

        while n!=0:
                r=n%10
                sum+=r
                n=int(n/10)
        
        return sum


ans=sumBase(79,3)
print(ans)

"""
Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base k.

After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.

 

Example 1:

Input: n = 34, k = 6
Output: 9
Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
Example 2:

Input: n = 10, k = 10
Output: 1
Explanation: n is already in base 10. 1 + 0 = 1
"""