package consistent_hashing

/**
参考文章
http://afghl.github.io/2016/07/04/consistent-hashing.html
http://afghl.github.io/2016/11/19/implement-consistent-hashing.html
 */

/**
传统 hash 方法是算出一个 object 的 hash 值然后与对应的 hash 空间（以下称 area）数量求余放入相应的 area 中
当 area 数量变换时候 object 的位置几乎要全变换
 */

/**
基本思路:
1. 把 object 求 hash（hash(object) 得到一个数字）；
2. 把 area 也求 hash，然后把 object 和 area 的 hash 值放入一个 hash 空间，
   通过一定的规则决定每个 object 落在哪一个 area 中。
 */