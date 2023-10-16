def sortTheStudents(score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        temp=[]
        dic={}
        res=[]
      

        for i in range(len(score)):

            temp.append(score[i][k])
            dic.update({score[i][k]:score[i]})


        
        
        temp.sort()
        temp.reverse()
        for x in temp:
              res.append(dic.get(x))

        
        return res

print(sortTheStudents(score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2))
