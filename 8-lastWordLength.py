def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        s=str(s)
        s=s.strip()
        l=s.split(" ")
        last=l[-1]
        # print(l)
        if last.isalpha():
                return len(last)
        # else:
        #         secondLast=l[-2]
        #         return len(secondLast)


length=lengthOfLastWord("hello this is cm    ")
print("the length of the last word is :",length)








"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


"""