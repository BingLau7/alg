package io.github.binglau.list;

import java.util.HashSet;
import java.util.Set;

/**
 * 类IntersectionOfTowLinkedList.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-09-05 下午9:09
 */
public class IntersectionOfTowLinkedList {
    public ListNode getIntersectionNodeByHashSet(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;
        Set<ListNode> set = new HashSet<ListNode>();
        ListNode t = headA;
        while (t != null) {
            set.add(t);
            t = t.next;
        }
        t = headB;
        while (t != null) {
            if (set.contains(t)){
                return t;
            }
            t = t.next;
        }
        return null;
    }

    public ListNode getIntersectionNodeByDiffLen(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;
        ListNode a = headA;
        ListNode b = headB;

        /**
         * 因为 aList.size + bList.size 是相等的,
         * 他们在第二次循环时候的c节点前是走了相同的步数的, 所以第二次循环结束时他们都是停在c节点处
         */
        while (a != b){
            a = a == null? headB : a.next;
            b = b == null? headA : b.next;
        }
        return a;
    }
}