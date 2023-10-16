def cal(n):
        count=0

        while(n>1):
            if(n%2==0):
                n=n/2
            else:
                n=(3*n)+1
            
            count+=1
        
        return count

def getKth(lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """

        ans=[]
        original=[]
   

        for i in range(lo,hi+1):
            temp=cal(i)
            ans.append(temp)
            
            original.append(i)

        
        copy=ans.copy()
     
        ans.sort()
        res=[]
        for e in ans:
            ind=copy.index(e)
            copy[ind]=0
            res.append(original[ind])
        
        return res[k-1]


print(getKth(12,15,2))
