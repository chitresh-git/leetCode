/* 
 * 143 solved 
 */


 class Linked {
    // 2130 solved
    ListNode head;

    class ListNode {
        int data;
        ListNode next;

        ListNode(int val) {
            data = val;
            next = null;
        }
    }

        void show(ListNode head) {
        ListNode n = head;

        while (n.next != null) {
            System.out.print(" " + n.data);
            n = n.next;
        }
        System.out.print(" " + n.data + "\n");
    }

    void insert(int data) {
        ListNode listnode = new ListNode(data);

        if (head == null) {
            head = listnode;
        } else {
            ListNode n = head;
            while (n.next != null) {
                n = n.next;
            }
            n.next = listnode;
        }
    }

    void fill() {
        for (int i = 0; i<10; i++) {
            insert(i);
        }
       
    }

    ListNode reversed;

    ListNode revert(int val){
        ListNode node=new ListNode(val);
        node.next=reversed;
        reversed=node;

        return reversed;

    }

    void reorder(){
         ListNode slow=head,fast=head;

        while(fast.next!=null ){
            fast=fast.next;
            if( fast.next!=null){
            slow=slow.next;
            fast=fast.next;
            }
        }

        ListNode left=head;
        ListNode right=slow.next;
        slow.next=null;
      
        ListNode ans=new ListNode(-1);
        ListNode temp=ans;

        while(right!=null){
            revert(right.data);
            right=right.next;
        }

        right=reversed;

        while(left!=null){
            temp.next=left;
            left=left.next;
            temp=temp.next;
            
            if(right!=null){
                
                temp.next=right;
                right=right.next;
                temp=temp.next;
                System.out.println(temp.data);
            }

        }

        ans=ans.next;
        head=ans;

        show(head);

        
    }

}

public class j158_reorderList {
    public static void main(String[] args) {
        Linked l=new Linked();
        l.fill();
        l.show(l.head);
        l.reorder();
    }
}

/* 
 * Medium
Topics
Companies
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 */
