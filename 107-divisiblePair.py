def countPairs(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        res=0

        for i in range(len(nums)-1):
                
                temp=[x for x in range(i+1,len(nums)) if nums[i]==nums[x] and (i*x)%k==0 ]

                # div=[x for x in temp if (i*x)%k==0]

                res+=len(temp)

        return res

print(countPairs(nums = [1,2,3,4], k = 1))

l=[[1,1],[1,2]]
l[1]-=1


print(l[0]==l[1])
print(l)