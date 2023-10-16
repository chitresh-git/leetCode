def defangIPaddr(address):
        """
        :type address: str
        :rtype: str
        """


        return address.replace(".","[.]")
    


     


ans=defangIPaddr("heloo.h.ey.")
print(ans)


"""
Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""