public class j165_removeStar {

    static String removeStars(String s) {
     StringBuilder res=new StringBuilder();

     for(int i=0;i<s.length();i++){
        if(s.charAt(i)=='*'){
            res.deleteCharAt(res.length()-1);
        }
        else{
            res.append(s.charAt(i));
        }
     }
        s=res.toString();
        return s;

    }

    public static void main(String[] args) {
        String ans = removeStars("leet**cod*e");

        System.out.println(ans);
    }

}

/* 
 * 2390. Removing Stars From a String
Solved
Medium
Topics
Companies
Hint
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
 */
