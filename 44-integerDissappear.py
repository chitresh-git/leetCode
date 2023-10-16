def findDisappearedNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=list(nums)
        n=len(nums)

        dis=[]
        i=1
        for e in nums:
                if nums.count(i)==0:
                        dis.append(i)
                i+=1
                
                
        return dis

ans=findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(ans)






