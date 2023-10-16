def countConsistentStrings(allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """

        res=0

        for e in words:
                flag=True
                e=set(e)
                e="".join(e)
               
                for i in e:
                  if i not in allowed:
                      
                        flag=False
                
                if flag : res+=1

        
        return res


ans=countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"])
print(ans)

"""
Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
"""
                        