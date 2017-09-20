package io.github.binglau.unkown;

/**
 * https://leetcode.com/problems/zigzag-conversion/#/solutions
 *
 *
 n=numRows
Δ=2n-2    1                           2n-1                         4n-3
Δ=        2                     2n-2  2n                    4n-4   4n-2
Δ=        3               2n-3        2n+1              4n-5       .
Δ=        .           .               .               .            .
Δ=        .       n+2                 .           3n               .
Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
Δ=2n-2    n                           3n-2                         5n-4

that's the zigzag pattern the question asked!
Be careful with nR=1 && nR=2

 没能理解 2n - 1 是怎么来的
 */
public class ZigZag {

    private static String zigZag(String s) {
        return "";
    }
}
