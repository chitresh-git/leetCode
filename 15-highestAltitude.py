def largestAltitude(gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        newl=[0]
        sum=0
        for e in gain:
                sum=sum+e
                newl.append(sum)
        
        high=max(newl)
        return high

ans=largestAltitude([-5,1,5,0,-7])
ans=largestAltitude([-4,-3,-2,-1,4,3,2])
print(ans)

'''
Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
'''