
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class ReverseLinkedList {
    int i = 1;
    /**
     **/
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null){
            return head;
        }
        ListNode p = head;
        ListNode q = head.next;
        ListNode r = q.next;
        ListNode t = null;
        p.next = null;
        while (r != null) {
            t = q;
            q.next = p;
            p = t;
            q = r;
            r = q.next;
        }
        q.next = p;
        return q;
    }

    public ListNode reverseList(ListNode head, int n, int m){
        ListNode _head = head;
        ListNode _tail = head;
        for (int i = 0; i < n - 1; i++) {
            _head = _head.next;
        }
        for (int i = 0; i < m - 1; i++) {
            _tail = _tail.next;
        }

        ListNode head_t = _tail;
        ListNode tail_t = null;
        tail_t = _tail.next;
        _tail.next = null;
        head_t = reverseList(_head);
        _head.next = head_t;
        ListNode _t = head_t;
        // while(_t != null) {
        //     System.out.println("------" + _t.val + ", " + _head.val);
        //     _t = _t.next;
        // }
        // _t.next = tail_t;
        // _t.next = head_t;
        return _t;
        // _t.next = _head;
        // while (_head.next != null){
        //     _head = _head.next;
        // }
        // _head.next = _tail;
        // return head;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        ListNode t = head.next;
        t.next = new ListNode(3);
        t = t.next;
        t.next = new ListNode(4);
        t = t.next;
        t.next = new ListNode(5);

        ReverseLinkedList r = new ReverseLinkedList();

        ListNode tt = r.reverseList(head, 2, 4);
        while(tt != null) {
            System.out.print(tt.val + " -> ");
            tt = tt.next;
        }
        System.out.println();
    }
}
