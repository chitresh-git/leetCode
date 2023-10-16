def multiply(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num1=int(num1)
        num2=int(num2)

        res=(num1*num2)
        return res

ans=multiply("10","20")
print(ans)


"""
Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
"""