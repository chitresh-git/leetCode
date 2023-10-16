
/* 1669 solved
 * class Solution {

    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode startprev=null,endahead=null;
        ListNode n= list1;
        ListNode newlist=list2;
        int counter=0;

         while(n.next!=null){
             if(counter==a-1){
                 startprev=n;
             }
             if(counter==b){
                 endahead=n.next;
             }
             n=n.next;
             counter++;
         }
         
         // merging the list with new list
         startprev.next=newlist;
         n=list1;
         while(n.next!=null){
             n=n.next;
         }
         n.next=endahead;
     
         return list1;
    }
}
 */
public class j151_merge {
    
}
