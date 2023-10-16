def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        l=list(s)
        sum=0
        lenght=len(l)
        for i in range(lenght):
            prev=0
            if i==0:
                prev=0
            else:
                prev=l[i-1]

            if l[i]=="I":
                sum=sum+1
            
            elif l[i]=="V":
                sum=sum+5
                if prev=="I":
                    sum=sum-1*2

            elif l[i]=="X":
                sum=sum+10
                if prev=="I":
                    sum=sum-1*2

            elif l[i]=="L":
                sum=sum+50
                if prev=="X":
                    sum=sum-10*2

            elif l[i]=="C":
                sum=sum+100
                if prev=="X":
                    sum=sum-10*2

            elif l[i]=="D":
                sum=sum+500
                if prev=="C":
                    sum=sum-100*2

            elif l[i]=="M":
                sum=sum+1000
                if prev=="C":
                    sum=sum-100*2
            print(sum)

            
        return sum

ans=romanToInt("MCMXCIV")
print(ans)