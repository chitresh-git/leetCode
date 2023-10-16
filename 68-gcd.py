def findGCD(nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        large=max(nums)
        small=min(nums)


        for e in range(small,0,-1):
                if small%e==0 and large%e==0:
                        return e

ans=findGCD([7,5,6,8,3])
print(ans)

""""
Example 1:

Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
Example 2:

Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.
Example 3:

Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3
"""