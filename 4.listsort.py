def merge(list1,list2):
    a,b=list(list1),list(list2)

    a.extend(b)
    a.sort()
    return a
    

sorted=merge([12,4,2,1,5],[1,4,2,6])

print(sorted)