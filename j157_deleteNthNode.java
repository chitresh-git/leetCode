public class j157_deleteNthNode{

}
/* 19 
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        
        
        ListNode start=new ListNode(-1);
        ListNode fast=start;
        ListNode slow=start;
        slow.next=head;


        for(int i=0;i<=n;i++){
            fast=fast.next;
        }

        while(fast!=null){
            fast=fast.next;
            slow=slow.next;
        }
        
        slow.next=slow.next.next;
return start.next;
        
        
    }
} */


/* Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1] */