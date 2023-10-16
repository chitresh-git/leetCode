def numJewelsInStones(jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        sum=0

        for e in jewels:
            sum=sum+stones.count(e)

        return sum

ans=numJewelsInStones("aA","aaaAdsds")
print(ans)


"""
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
"""