
class Linked {
    // 92 correct but time limit exceeded
    Node head;

    class Node {
        int data;
        Node next;

        Node(int val) {
            data = val;
            next = null;
        }
    }

    void insert(int val) {
        Node node = new Node(val);

        if (head == null) {
            head = node;
        } else {
            Node n = head;
            while (n.next != null) {
                n = n.next;
            }
            n.next = node;
        }
    }

    void fill() {
        for (int i = 0; i<10; i++) {
            insert(i);
        }
       
    }

    void show(Node head) {
        Node n = head;

        while (n.next != null) {
            System.out.print(" " + n.data);
            n = n.next;
        }
        System.out.print(" " + n.data + "\n");
    }

    Node reversed;
    

    Node reverse(int val){
        Node node=new Node(val);

        
            node.next=reversed;
            reversed=node;
            return reversed;
  

    }

    void callReverse(int left,int right){
        Node n=head;
        Node headpart=n,tailPart=n;
        Node temp=head;

        while(n.next!=null){
            if(n.next.data<left){
                headpart=headpart.next;
            }
            
            if(n.data>=left && n.data<=right){
                temp=reverse(n.data); // reversing desired part of the linked list
            }
            if(n.data>right){
                tailPart=n;
                break;
            }
            
    
            n=n.next;
        }
       // joining the new linked list
        headpart.next=temp;
        n=temp;
        while(n.next!=null){
            n=n.next;
        }
        n.next=tailPart;
       

        


        }


    }


public class j147_reverse {
    public static void main(String[] args) {
        Linked list=new Linked();
        list.fill();
        list.show(list.head);
        list.callReverse(2, 6);
        list.show(list.head);
    }
}
