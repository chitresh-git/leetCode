def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """

        c=str(s)
        ind=0
        for e in c:
                if c.count(e)==1:
                        return ind
                ind+=1
        
        return -1

ans=firstUniqChar("aabb")
print(ans)

"""
Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""