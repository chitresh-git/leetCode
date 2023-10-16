def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
       
    try:
        n=list(nums)
        low=n.index(target)
        high=low
        for i in range(len(n)-1,low,-1):
                print(n[i])
                if n[i]==target:
                        high=i
                        break;
        
        return [low,high]
    except :
        return [-1,-1]

res=searchRange([1,2,3,4,3,0,0,3,5],9)
print(res)