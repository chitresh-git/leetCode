def truncateSentence(s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        l=s.split()

        res=""

        for i in range(k):
            res=res+" "+l[i]

        return res.strip()

ans=truncateSentence(" this is my code " , 2)
print(ans)

"""
Example 1:

Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"
Explanation:
The words in s are ["Hello", "how" "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".
Example 2:

Input: s = "What is the solution to this problem", k = 4
Output: "What is the solution"
Explanation:
The words in s are ["What", "is" "the", "solution", "to", "this", "problem"].
The first 4 words are ["What", "is", "the", "solution"].
Hence, you should return "What is the solution".
Example 3:

Input: s = "chopper is not a tanuki", k = 5
Output: "chopper is not a tanuki"
"""