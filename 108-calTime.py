def minTimeToVisitAllPoints(points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        count=0

        for i in range(len(points)-1):
                
                temp=points[i][0]-points[i][1]

                count+=temp

                temp=abs(points[i][1]-points[i+1][0])

                count+=temp
                print(count)

        count+=points[-1][0]-points[-1][1]

        return count


print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))

