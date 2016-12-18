package io.github.binglau.interview;

import java.util.ArrayList;
import java.util.List;

/**
 * 类ListReciprocalK.java的实现描述：TODO:类实现描述
 * 求链表倒数第K位
 *
 * @author bingjian.lbj 2016-12-18 下午3:07
 */
public class ListReciprocalK {

    public static <T> T listReciprocalK(List<T> list, int k) {
        if (list == null || list.size() < k || k < 1) return null;
        int i = 0;
        for (int j = k; j < list.size(); i++, j++);
        return list.get(i);
    }

    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(3);
        list.add(7);
        list.add(4);
        list.add(9);
        list.add(0);
        list.add(2);
        System.out.println(listReciprocalK(list, 2));
        System.out.println(listReciprocalK(list, 4));
        System.out.println(listReciprocalK(list, -1));
        System.out.println(listReciprocalK(list, 0));
        System.out.println(listReciprocalK(list, 304));
    }
}
