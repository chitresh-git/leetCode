// 2487
/* 
 * 
class Solution {
    ListNode reversed;
   
    ListNode result;
    



ListNode reverse(ListNode temphead, int data){
    ListNode node=new ListNode(data);
    node.next=temphead;
    temphead=node;
    return temphead;

}
    public ListNode removeNodes(ListNode head) {
        ListNode n=head;
        while(n!=null){
           reversed= reverse(reversed,n.val);
            n=n.next;

        }
       
        ListNode node=reversed;
        ListNode forward=reversed.next;
           while(forward!=null){

               if(node.val>forward.val){
                   node.next=forward.next;
                   forward=forward.next;
               }
               else{
                   node=node.next;
                   forward=forward.next;
               }

        }
        n=reversed;
           while(n!=null){
           result= reverse(result,n.val);
            n=n.next;

        }

        return result;
    }
}
 */

public class j156_deleteNthNode{

}
/* You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105 */