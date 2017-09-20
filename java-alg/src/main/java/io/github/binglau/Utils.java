package io.github.binglau;

import java.util.HashMap;

class A {
    private String a;
    private String b;
    private String c;
    private String d;

    public A(String a, String b, String c, String d) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
    }

    @Override
    public String toString() {
        return "A{" +
                "a='" + a + '\'' +
                ", b='" + b + '\'' +
                ", c='" + c + '\'' +
                ", d='" + d + '\'' +
                '}';
    }
}

public class Utils {
    public static int[] swap(int i, int j) {
        return new int[] {j, i};
    }

    public static void main(String[] args) {
        A a = new A(null, "", "", "");
        System.out.println("主函数中的a: " + a);
        function(a);
        System.out.println("主函数中的a,经过function处理后: " + a);
    }

    static void function(A a) {
        A a2 = new A("a", "b", "c", "d");
        a = a2;
        System.out.println("function中的a: " + a);
    }
}
