def arrayStringsAreEqual(word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """



        one,two="".join(word1),"".join(word2)
       
        if one==two: return True
        else: False



ans=arrayStringsAreEqual(["a","b"],["ab"])
print(ans)


"""
Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
"""

        