package io.github.binglau.sort;

import java.util.Arrays;

public class QuickSort {

    public static void quickSort(int[] arr){
        quickSort(arr, 0, arr.length - 1);
    }

    private static void quickSort(int[] arr, int left, int right){
        if (left < right){
            int pivotIndex=partition(arr, left, right);
            quickSort(arr, left, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, right);
        }
    }
    private static int partition(int[] arr, int left, int right) {
        int pivot = arr[left];
        int tmp, m = left + 1;
        for (int i = left + 1; i <= right; i++) {
            if (pivot >= arr[i]) {
                tmp = arr[i];
                arr[i] = arr[m];
                arr[m] = tmp;
                m++;
            }
        }
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
