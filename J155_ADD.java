public class J155_ADD {
    
}
/* 2 solved
 * class Solution {
    ListNode rev;
    void reverse(int data){
        ListNode node=new ListNode(data);
        if(rev==null)
        rev=node;
        else{

        ListNode n=rev;
        while(n.next!=null){
            n=n.next;
        }
        n.next=node;
        }
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode one ,two;
        one =l1;
        two=l2;

        int carry=0,temp=0;
        while(one!=null && two!=null){
            temp=one.val+two.val;
            temp+=carry;
          
            if(temp>9){
                carry=1;
                temp=temp%10;

            }
            else{
                carry=0;
            }
            reverse(temp);
            one=one.next;
            two=two.next;
        }

          while(one!=null){
            temp=one.val;
            temp+=carry;
          
            if(temp>9){
                carry=1;
                temp=temp%10;

            }
            else{
                carry=0;
            }
            reverse(temp);
            one=one.next;
            
        }

          while(two!=null){
            temp=two.val;
            temp+=carry;
           
            if(temp>9){
                carry=1;
                temp=temp%10;

            }
            else{
                carry=0;
            }
            reverse(temp);
           
            two=two.next;
        }

        if(carry>0)
        reverse(carry);

        return rev;
                 
    }
}
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 */