def maxCoins(piles):
        """
        :type piles: List[int]
        :rtype: int
        """

        piles=list(piles)
        piles.sort()
        piles.reverse()
        print(piles)

        sum,ind,times=0,1,int(len(piles)/3)

        for i in range(times):
                sum+=piles[ind]
                ind+=2


        return sum

ans=maxCoins([2,4,5])
print(ans)