def findDelayedArrivalTime(arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """

        newt=arrivalTime+delayedTime

        if newt == 24:
            return 0
        elif newt> 24:
            return newt-24
        else:
            return newt

ans=findDelayedArrivalTime(12,24)
print(ans)

"""
Example 1:

Input: arrivalTime = 15, delayedTime = 5 
Output: 20 
Explanation: Arrival time of the train was 15:00 hours. It is delayed by 5 hours. Now it will reach at 15+5 = 20 (20:00 hours).
Example 2:

Input: arrivalTime = 13, delayedTime = 11
Output: 0
Explanation: Arrival time of the train was 13:00 hours. It is delayed by 11 hours. Now it will reach at 13+11=24 (Which is denoted by 00:00 in 24 hours format so return 0).
"""