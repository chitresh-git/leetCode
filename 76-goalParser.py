def interpret(command):
        """
        :type command: str
        :rtype: str
        """


        command=command.replace("()","o")
        
        return command.replace("(al)","al")


ans=interpret("(al)G(al)()()G")
print(ans)











"""
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
"""