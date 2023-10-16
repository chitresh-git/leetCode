def destCity(paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """

        prev=paths[0][1]
        for i in range(len(paths)-1) :
               

                if prev==paths[i+1][0]:
                        print(i)
                        prev=paths[i+1][1]
                        print(prev)
        

        return prev



ans=destCity([["qMTSlfgZlC","ePvzZaqLXj"],["xKhZXfuBeC","TtnllZpKKg"],["ePvzZaqLXj","sxrvXFcqgG"],["sxrvXFcqgG","xKhZXfuBeC"],["TtnllZpKKg","OAxMijOZgW"]])
print(ans)

                        