def countDistinctIntegers(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

     
        copy=nums.copy()
        for e in copy:
           
                sum=0
                
                while e!=0:
                        r=e%10
                        sum=sum*10 + r
                        e=int(e/10)
                
                nums.append(sum)
        
        nums=len(set(nums))

        return nums

ans=countDistinctIntegers([2,2,2])
print(ans)


"""
Example 1:

Input: nums = [1,13,10,12,31]
Output: 6
Explanation: After including the reverse of each number, the resulting array is [1,13,10,12,31,1,31,1,21,13].
The reversed integers that were added to the end of the array are underlined. Note that for the integer 10, after reversing it, it becomes 01 which is just 1.
The number of distinct integers in this array is 6 (The numbers 1, 10, 12, 13, 21, and 31).
Example 2:

Input: nums = [2,2,2]
Output: 1
Explanation: After including the reverse of each number, the resulting array is [2,2,2,2,2,2].
The number of distinct integers in this array is 1 (The number 2).
"""
                        