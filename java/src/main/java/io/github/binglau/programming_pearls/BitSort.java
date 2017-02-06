package io.github.binglau.programming_pearls;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.BitSet;
import java.util.Random;

public class BitSort {
    public static void bitSort(int[] data, int max) {
        // 创建一个max的数组，默认都为0
        BitSet r = new BitSet(max);

        for (int i = 0; i < data.length; i++) {
            r.set(data[i]);
        }

        for (int i = 0; i < r.length(); i++) {
            if (r.get(i))
                System.out.print(i + " ");
        }
    }

    public static void main(String[] args) {
        // 实验一个100以内的排序
        int max = 100;
        Random random = new Random(47);
        int[] data = new int[30];
        for (int i = 0; i < data.length; i++) {
            data[i] = random.nextInt(max);
        }
        System.out.println(Arrays.toString(data));
        bitSort(data, max);
    }
}
