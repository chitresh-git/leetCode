def removeTrailingZeros(num):
        """
        :type num: str
        :rtype: str
        """

        num=list(num)

        num.reverse()
        count=0

        for e in num:
                if e=="0":
                        count+=1
                else:
                        break
        
        for i in range(count):
                num.remove("0")
        
        num.reverse()
        num="".join(num)

        return num

ans=removeTrailingZeros("51230100")
print(ans)
        