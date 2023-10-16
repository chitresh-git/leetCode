def isSubsequence(s,t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        k,j=0,0
        try: 
          while len(s)>k:
              if t[j]==s[k]: k+=1
              j+=1
             
        except:  return False
        
        if k==len(s): return True
        else: return False

        

        

ans=isSubsequence('acb', 'ahbgdc')
print(ans)


"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""
                        