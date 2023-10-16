def maximumUnits(boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        not solved
        1710
        """

        temp,dic,usedTruck,units=[],{},0,0

        for x in boxTypes:
                
                 
                if x[1] in temp:
                       v=0
                       v+=dic.get(x[1])
                       dic.update({x[1]:v})
                else:
                        dic.update({x[1]:x[0]})
                temp.append(x[1])
         
        temp.sort()
        temp.reverse()
        print(dic)
        print(temp)

        for x in temp:
                if usedTruck+dic.get(x)<=truckSize:
                        units+=x*dic.get(x)
                        usedTruck+=dic.get(x)
                        print(units,usedTruck)
                
                else:
                        print(x)
                        print(truckSize-usedTruck)
                        units+=(truckSize-usedTruck)*x
                        return units

        return units

print(maximumUnits(boxTypes =[[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]],truckSize =35))



        