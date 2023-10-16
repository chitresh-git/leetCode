def sortPeople(names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        d={}

        for k,v in zip(heights,names):
                d.update({k:v})

        heights.sort()

        res=[d.get(i) for i in heights]

        res.reverse()
        return res

print(sortPeople(["Alice","Bob","Bob"], heights = [155,185,150]))

"""
Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
"""
                
