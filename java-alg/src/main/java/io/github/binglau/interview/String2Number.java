package io.github.binglau.interview;

/**
 * 类String2Number.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-12-18 下午1:32
 */
public class String2Number {
    private static boolean isNumber(char i){
        return i >= '0' && i <= '9';
    }

    /**
     *  1. 考虑正负数
     *  2. 考虑首位为0
     *  3. 考虑字符串非数字
     *  4. 考虑字符串为null
     *  5. 如果是意外情况抛出异常
     */
    public static int string2Number(String number) {
        int result = 0;
        if (number == null) throw new RuntimeException("不可转换");
        if (number.charAt(0) != '-' && !isNumber(number.charAt(0)) ) throw new RuntimeException("不可转换");
        if (number.charAt(0) == '-' && number.length() == 1) throw new RuntimeException("不可转换");
        // 处理-0的情况
        if (number.charAt(0) == '-' && number.length() == 2 && number.charAt(1) == '0') return 0;
        // i用于移动number字符, j用于记录位数
        for (int i = 0; i < number.length(); i++) {
            if (i == 0 && (number.charAt(i) == '-' || number.charAt(i) == '0')) continue;
            if (i > 0 && !isNumber(number.charAt(i))) throw new RuntimeException(("不可转换"));
            result = result * 10 + (number.charAt(i) - '0');
        }

        // 负数情况
        if (number.charAt(0) == '-') result = result * -1;

        return result;
    }

    public static void main(String[] args) {
//        System.out.println(string2Number("123"));
//        System.out.println(string2Number("-123"));
//        System.out.println(string2Number("-0123"));
//        System.out.println(string2Number("0123"));
//        System.out.println(string2Number("123ejkl"));
        System.out.println(string2Number("-oejkl"));
    }
}
