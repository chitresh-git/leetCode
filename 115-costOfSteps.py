def minCostClimbingStairs(cost):
        """
        :type cost: List[int]
        :rtype: int
        not solved 
        746
        """

        if len(cost)<=3:
                return min(cost[1:2])

       
        s=0
        i=0
        if cost[0]>=cost[1]:
                s=cost[1]
                i=1
        else:
                s=cost[0]
                i=0

        print(s)

        while i < len(cost)-2:

                if cost[i+1]>=cost[i+2]:
                        s+=cost[i+2]
                        i+=2

                else:
                        s+=cost[i+1]
                        i+=1
                
                print(s)

                

        return s

print(minCostClimbingStairs([0,1,2,2]))
