def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """

        s=str(s)

        s=s.strip()
        
        s=s.split()
        s.reverse()

        result=" ".join(s)
        # result=" ".join(result.split())

        return result

ans=reverseWords("a good   example")
print(ans)

'''
Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
'''