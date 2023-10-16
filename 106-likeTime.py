def maxSatisfaction(satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """

        satisfaction.sort()

        res=[]
        

        k=0
        

        for i in range(len(satisfaction)):
                sum=0
                count=1
                for j in range(i,len(satisfaction)):
                        
                        sum+=satisfaction[j]*count
                        count+=1

                res.append(sum)

        ans=max(res)

        if ans<=0:return 0
        else: return ans

print(maxSatisfaction([-1,-4,-5]))
                