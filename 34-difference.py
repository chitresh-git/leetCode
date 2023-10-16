def findTheDifference(s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        for e in t:
            if s.count(e)!=t.count(e):    return e

        
ans=findTheDifference("abcd","abcde")
print(ans)
print(type(ans))



"""
Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
"""