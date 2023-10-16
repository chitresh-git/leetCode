
def reverseVowels(s):
        """
        :type s: str
        :rtype: str
        """
        s=str(s)
        vow=[]
        allvowels=('a','A','e','E','i','I','o','O','u','U')
        for e in s:
                if e in allvowels:
               
                       
                        vow.append(e)


        print(vow)
        vow.reverse()
        print(vow)
        j=0
        m=""
        for i in range(len(s)):
                if s[i] in allvowels:
                        m=m+vow[j]
                        j+=1
                
                else:
                        m=m+s[i]
                        
        return m

ans=reverseVowels("rashi dashore")
print(ans)


"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
"""      


                        