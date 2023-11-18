public class j170_1047 {
    /* 
     * 1047. Remove All Adjacent Duplicates In String
Solved
Easy
Topics
Companies
Hint
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
     */
}
/* 
 * class Solution {

    public String removeDuplicates(String s) {
 StringBuilder res=new StringBuilder();
 res.append(s.charAt(0));

        for(int i=1;i<s.length();i++){
       
            if(res.length()>0 && s.charAt(i)==res.charAt(res.length()-1)){
                res.deleteCharAt(res.length()-1);            
                
            }
            else{
                res.append(s.charAt(i));
            }
     
        }

        s=res.toString();
        return s;
    }
}
 */
