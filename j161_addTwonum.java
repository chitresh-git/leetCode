public class j161_addTwonum {
    
}

/* 
 * class Solution {
   
    ListNode reverse(int data,ListNode head2){
        ListNode node=new ListNode(data);

        node.next=head2;
        head2=node;
        return head2;
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode t1=null,t2=null;

        while(l1!=null || l2!=null){
            if(l1!=null){
               t1= reverse(l1.val,t1);
               l1=l1.next;
            }
            if(l2!=null){
                t2=reverse(l2.val,t2);
                l2=l2.next;
            }
        }

    
        
        int carry=0,temp=0;
        ListNode ans=null;

        while(t1!=null || t2!=null){
            if(t1!=null && t2!=null){
            temp=t1.val+t2.val;
                   //System.out.println("h"+temp);

            t1=t1.next;
            t2=t2.next;

            }
            else if(t1==null && t2!=null){
                temp=t2.val;
                t2=t2.next;
 
            }
            else if(t2==null && t1!=null){ 
                temp=t1.val;
                t1=t1.next;
                
            }
            temp+=carry;
            if(temp>9){
            temp=temp%10;
            carry=1;
            }
            else{
            carry=0;
            }
            ans=reverse(temp,ans);
   
            

        }
        if(carry!=0)
        ans=reverse(carry,ans);
        
        return ans;
     
    }
}


 */

 /* 


445. Add Two Numbers II
Solved
Medium
Topics
Companies
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0] */