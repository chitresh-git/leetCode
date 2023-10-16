def countAndSay(n):
        """
        :type n: int
        :rtype: str
        """

        s=str(n)
        m=""
        l=[]
        
        for i in range(n):
                # m=s
                sorted=[]
                for j in s:
                        if j not in sorted:
                                sorted.append(j)
                print(sorted)
                        
               
                
                
                for i in range(len(s)) :
                        # print(e)
                    e=s[i]
                    if e!=s[i-1]:
                        c=str(s.count(e))
                        s=s.replace(e,"")
                        # print(m)
                        
                        m=m+c+e
                        # print(m)
                print(m)
                s=m
                m=""
                # print(s)

        print(m)

countAndSay(4)
                        