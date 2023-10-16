def strStr(haystack, needle):
        
    try:
        haystack=str(haystack)
        ind=haystack.index(needle)
        return ind
    
    except Exception as e :
        return -1
    

a=strStr("helloelel","i")
print(a)