def minSteps( s, t):
        
        # not solved

        """
        :type s: str
        :type t: str
        :rtype: int
        """
        letters={}
        count=0

        for e in set(s):
                print(e)
                letters.update({e:s.count(e)})
        print(letters)

        for e in set(t):
                if e not in s:
                        count+=t.count(e)
                else :
                    if letters.get(e)>t.count(e):
                        temp=letters.get(e)-t.count(e)
                        # if temp>0:
                        count+=temp
                        print("count=",count)
                
        return count


ans=minSteps("leetcode", t = "practice")
print(ans)