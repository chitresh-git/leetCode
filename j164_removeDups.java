public class j164_removeDups{
    /*  correct but time exceeded
     *     public ListNode deleteDuplicates(ListNode head) {
        ListNode n=head.next;
        ListNode prev=head;
        
        int count=0;
        while(n!=null){
           count=0;
            if(n.next!=null){

            while(n.val==n.next.val){
                count++;
                n=n.next;
            }

            }

            if(count>0){
            prev.next=n.next;
            prev=prev.next;
            }
            else{
            prev.next=n;
            prev=prev.next;
            }


            n=n.next;

        }
        
        return head;
    }
     */
}