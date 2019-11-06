"""
954. 二倍数对数组


给定一个长度为偶数的整数数组 A，只有对 A 进行重组后可以满足 “对于每个 0 <= i < len(A) / 2，
都有 A[2 * i + 1] = 2 * A[2 * i]” 时，返回 true；否则，返回 false。

示例 1：
输入：[3,1,3,6]
输出：false

示例 2：
输入：[2,1,2,6]
输出：false

示例 3：
输入：[4,-2,2,-4]
输出：true
解释：我们可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]

示例 4：
输入：[1,2,4,16,8,4]
输出：false

提示：
0 <= A.length <= 30000
A.length 为偶数
-100000 <= A[i] <= 100000
"""


class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 0:
            return True

        positive = []
        negative = []
        ad = {}

        for a in A:
            ad[a] = ad.get(a, 0) + 1
            if a < 0:
                negative.append(a)
            else:
                positive.append(a)

        lp = len(positive)
        # ln = len(negative)s

        if lp % 2 != 0:
            return False

        positive.sort()
        negative.sort(reverse=True)

        for p in positive:
            if ad[p] > 0:
                if p * 2 in ad:
                    ad[p] = ad[p] - 1
                    ad[p * 2] = ad[p * 2] - 1
                else:
                    return False
                    break
            else:
                continue
        for n in negative:
            if ad[n] > 0:
                if n * 2 in ad:
                    ad[n] = ad[n] - 1
                    ad[n * 2] = ad[n * 2] - 1
                else:
                    return False
                    break
            else:
                continue

        return all([v == 0 for v in ad.values()])


s = Solution()
# print(s.canReorderDoubled([3, 1, 3, 6]))
# print(s.canReorderDoubled([2, 1, 2, 6]))
# print(s.canReorderDoubled([4, -2, 2, -4]))
# print(s.canReorderDoubled([1, 2, 4, 16, 8, 4]))
# print(s.canReorderDoubled([1, 2, 4, 8]))
print(s.canReorderDoubled([-4, -6, -1, -2, -1, -1, -3, -8]))
"""
此题解法：
* 一定是要使用字典的。字典存放A数组中的数字和出现的次数
* 将字典排序，排序的key= lambda x: abs(x)使用键值的绝对值排序，这样就解决掉了负数逆序的问题
* 依次遍历排序的字典（从小到大）

       from collections import Counter
       A_dict = Counter(A)

        for x in sorted(A_dict, key=lambda x: abs(x)):
            if A_dict[x] > A_dict[2*x]:
                return False

            A_dict[2*x] -= A_dict[x]
        return True

* 这里利用Counter字典的特性，访问不存在键值是返回0，而非错误
* 如果d[x] > d[x*2] 就说明没有足够的2倍键值的数字存在，反之就用d[x*2]-d[x]，
  表示用掉了x个数的双倍键值。
"""
