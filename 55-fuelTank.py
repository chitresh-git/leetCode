def distanceTraveled(mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        copy=mainTank
        c2=additionalTank

        for i in range(1,mainTank+1):
                print(i)
                
                if i%5==0:
                    print(i)
                    if additionalTank>0:
                        mainTank+=1
                        additionalTank-=1
                        print(mainTank,additionalTank)
                    else:
                        #   break
                        pass
        print(mainTank)
        
        ef=int(mainTank/5)
        if ef>=c2:

         mainTank=copy+c2
        
        else:
                mainTank=copy+ef
        print(mainTank)
                        




        return mainTank*10

ans=distanceTraveled(29,7)
print(ans)