def merge(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        newList=[]
        i=0
        for i  in  range(len(intervals)-1):
                newin=[]
                print(out[1])
                print(intervals[i+1][0])

                if out[1]>=intervals[i+1][0]:
                        newin.append(out[0])
                        newin.append(intervals[i+1][1])
                        newList.append(newin)
                else:
                        newList.append(out)
                i+=1
                
               
        return newList

ans=merge([[1,3],[2,6],[8,10],[15,18]])
print(ans)
                
                        