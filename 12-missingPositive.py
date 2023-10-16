def firstMissingPositive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=list(nums)

        for i in range(1,len(l)+1):
                print
                if l.count(i)==0:
                        return i
              
        return len(l)+1

res=firstMissingPositive([7,8,9,11,12])
print(res)