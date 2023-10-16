def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        2529
        """
        a=[]
        a.reverse()
        s=""
        s.isnumeric()
        ps,ng=0,0
        for i in nums:
            if i>0:
                ps+=1
            if i<0:
                ng+=1

        if ps>ng:return ps

        else:return ng

       

            
        