def numberOfMatches(n):
        """
        :type n: int
        :rtype: int
        """

        team=0

        while n>1:
            if n%2==0:
                n=n/2
                team=team+n
            else:
                n=(n-1)/2
                team=team+n+1

        return team

ans=numberOfMatches(12121)
print(ans)