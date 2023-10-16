def countDigits(num):
        """
        :type num: int
        :rtype: int
        """
        copy,count=num,0

        while num!=0:
                r=num%10

                if  copy%r==0:
                        count+=1
                
                num=int(num/10)
        
        return count

ans=countDigits(1248)
print(ans)

"""
Example 1:

Input: num = 7
Output: 1
Explanation: 7 divides itself, hence the answer is 1.
Example 2:

Input: num = 121
Output: 2
Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
Example 3:

Input: num = 1248
Output: 4
Explanation: 1248 is divisible by all of its digits, hence the answer is 4.
"""