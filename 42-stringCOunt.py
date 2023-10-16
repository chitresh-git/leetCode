def countSegments(s):
        """
        :type s: str
        :rtype: int
        """
        s=str(s)
        s=s.strip()

        if s=="":
            return 0

        l=s.split()
        space=l.count("")
        print(l)
     

        return len(l)


ans=countSegments(", , , ,        a, eaefa")
print(ans)


""""
Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:

Input: s = "Hello"
Output: 1
"""