def maximum69Number (num):
        """
        :type num: int
        :rtype: int
        """

        num=str(num)

  

        num=num.replace("6","9",1)
        return int(num)

ans=maximum69Number(9669)
print(ans)

