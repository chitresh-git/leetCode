class Linked {
    // 2181 correct but time limit exceeded
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

    Node answer;
    
    void insertNew(int val) {
        Node node = new Node(val);

        if (answer == null) {
            answer= node;
        } else {
            Node n = answer;
            while (n.next != null) {
                n = n.next;
            }
            n.next = node;
        }
    }
void merge(){
    Node n=head.next;
    Node zero=n;
 
    int sum=0;
    while(n.next!=null){
        if(n.data==0){
            zero.data=sum;
            zero=n;
            
        }
       
        if(n.data!=0){
         
            sum+=n.data;
            n=n.next;
        }
        if(n.next.data==0){
            zero.next=n.next;
        }
    

        
      
    }
  
}



    }

public class j149_merge2{
    public static void main(String[] args) {
        Linked list=new Linked();
        list.insert(0);
        list.insert(1);
        list.insert(2);
        list.insert(0);
        list.insert(3);
        list.insert(4);
        list.insert(5);
        list.insert(0);

        list.show(list.head);
        list.merge();
        list.show(list.head);
    }
}
