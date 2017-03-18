package io.github.binglau.sort;

import java.util.Arrays;

public class QuickSort {

    public static void quickSort(int[] arr){
        quickSort(arr, 0, arr.length - 1);
    }

    private static void quickSort(int[] arr, int left, int right){
        if (left < right){
            int pivot=partition(arr, left, right);
            quickSort(arr, left, pivot - 1);
            quickSort(arr, pivot + 1, right);
        }
    }
    private static int partition(int[] arr, int left, int right) {
        int pivot = arr[left];
        // m 为标记最近一个比主要大的数
        // i 为前遍历数的索引
        int m = left + 1, i;
        int tmp;
        for (i = left + 1; i <= right; i++) {
            if (pivot > arr[i]) {
                // m 与 i 互换
                tmp = arr[i];
                arr[i] = arr[m];
                arr[m] = tmp;
                m += 1;
            }
        }
        // 主元与 m 前的元素互换
        tmp = arr[left];
        arr[left] = arr[m - 1];
        arr[m - 1] = tmp;
        return m - 1;
    }

    public static void main(String[] args) {
        int[] data = new int[]{12, 31, 3, 18, 9, 23, 1, 4, 11};
        quickSort(data);
        System.out.println(Arrays.toString(data));
    }

}
