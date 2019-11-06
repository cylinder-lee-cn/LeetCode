"""
970. 强整数

给定两个非负整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，
那么我们认为该整数是一个强整数。

返回值小于或等于 bound 的所有强整数组成的列表。
你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。

示例 1：
输入：x = 2, y = 3, bound = 10
输出：[2,3,4,5,7,9,10]
解释：
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2

示例 2：
输入：x = 3, y = 5, bound = 15
输出：[2,4,6,8,10,14]

提示：
1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6
"""


class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        result = set()

        if x == 0 and y == 0:
            return [n for n in [0, 1, 2] if n <= bound]
        elif x == 0 and y == 1:
            return [n for n in [1, 2] if n <= bound]
        elif x == 1 and y == 0:
            return [n for n in [1, 2] if n <= bound]
        elif x == 1 and y == 1:
            return [n for n in [2] if n <= bound]
        elif x == 1 or y == 1:
            z = max(x, y)
            i, sumxy = 0, z**0 + 1
            while bound >= sumxy:
                result.add(sumxy)
                i = i + 1
                sumxy = z**i + 1
            return list(result)
        else:
            i, sumxy = 0, x**0 + 1
            while bound > (x**i + 1):
                j = 0
                sumxy = x**i + 1
                while bound >= sumxy:
                    result.add(sumxy)
                    j = j + 1
                    sumxy = x**i + y**j
                i = i + 1
            return list(result)


s = Solution()
# print(s.powerfulIntegers(2, 3, 10))
# print(s.powerfulIntegers(3, 5, 15))
print(s.powerfulIntegers(1, 2, 100))

"""
此题解法：
* 题目说明 0 <= bound <= 10^6 ，所以只要算到2^18即可。
* 利用set来过滤重复的结果
* 然后用暴力法即可

        ans = set()
        # 2**18 > bound
        for i in range(18):
            for j in range(18):
                v = x**i + y**j
                if v <= bound:
                    ans.add(v)
        return list(ans)
"""
