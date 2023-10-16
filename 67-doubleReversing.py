def isSameAfterReversals(num):
        """
        :type num: int
        :rtype: bool
        """

        if num==0:
            return True

        num=list(str(num))

 
        
        if num[-1]=="0":
                return False
        
        return True


ans=isSameAfterReversals(1200)
print(ans)

"""
Example 1:

Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.
Example 2:

Input: num = 1800
Output: false
Explanation: Reverse num to get 81, then reverse 81 to get
"""