def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=len(nums)-1
        i=0
        while i<l:
            print(i,l)
            if nums.count(nums[i])>1:
                return True
            elif nums.count(nums[l])>1:
                return True
            
            i+=1
            l-=1


        return False

ans=containsDuplicate([1,2,3,4,5,1])
print(ans)


"""
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
"""