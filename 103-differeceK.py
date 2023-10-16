def countKDifference(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        i,res=0,0

        for i in range(len(nums)):

             for j in range(i+1,len(nums)):
                    # print(nums[i],nums[j])
                    if abs(nums[i]-nums[j])==k:
                           
                           res+=1

        
        return res

print(countKDifference(nums = [1,2,2,1], k = 1))

