def maximumWealth(accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        res=0

        for x in accounts :
            temp=0
            for e in x :
                temp+=e
                if temp> res:
                    res=temp

        return res


ans=maximumWealth([[1,5],[7,3],[3,5]])
print(ans)

