def shuffle( nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        start=nums[:n]
        end=nums[n:]
        res=[]

        for i,j in zip(start,end):
                res.append(i)
                res.append(j)

        return res


ans=shuffle([2,5,1,3,4,7], n = 3)
print(ans)
                

        