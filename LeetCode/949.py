"""
949. 给定数字能组成的最大时间

给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。

最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。

以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。

示例 1：
输入：[1,2,3,4]
输出："23:41"

示例 2：
输入：[5,5,5,5]
输出：""

提示：
A.length == 4
0 <= A[i] <= 9
"""


class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        import itertools

        atime = itertools.permutations(A)
        result = []

        def vaildtime(ts):
            if (ts[0] == 2):
                if (ts[1] in [0, 1, 2, 3]):
                    if (ts[2] in [0, 1, 2, 3, 4, 5]):
                        return str(ts[0]) + str(ts[1]) + ':' + str(
                            ts[2]) + str(ts[3])
                    else:
                        return ''
                else:
                    return ''
            elif (ts[0] == 0 or ts[0] == 1):
                if (ts[2] in [0, 1, 2, 3, 4, 5]):
                    return str(ts[0]) + str(ts[1]) + ':' + str(ts[2]) + str(
                        ts[3])
                else:
                    return ''
            else:
                return ''

        for t in atime:
            result.append(vaildtime(t))

        return sorted(result)[-1]


s = Solution()
print(s.largestTimeFromDigits([1, 2, 3, 4]))
print(s.largestTimeFromDigits([5, 5, 5, 5]))
print(s.largestTimeFromDigits([4, 0, 0, 0]))
print(s.largestTimeFromDigits([6, 2, 6, 0]))
"""
此题解法：
* 24小时制，小时2位，第一位[2，1，0]，第二位[3，2，1，0]
* 分钟两位，第一位[5，4，3，2，1，0]，第二位[9，8，7，6，5，4，3，2，1，0]
* {2:[3,2,1,0],[1-0]:[9-0],[5-0]:[9-0]}

* 一种解法是使用字典来生产所有1440分钟对应的时间字符串
* 利用itertools来生成所有24中组合，然后看看哪些在字典中

        import itertools
        everymin = {}
        gettime = {}

        i = 0
        keymax = 0

        for h in range(24):
            for m in range(60):
                tmp = str(h).zfill(2) + str(m).zfill(2)
                everymin[tmp] = i
                i = i + 1
        # print(len(everymin))

        atime = itertools.permutations(A)

        for t in atime:
            tt = ''.join(str(x) for x in list(t))
            if (tt in everymin):
                gettime[everymin[tt]] = tt
                keymax = max(everymin[tt], keymax)

        if (len(gettime) > 0):
            timemax = gettime[keymax]
            return timemax[0:2] + ':' + timemax[2:]
        else:
            return ''

* 第二种解法：
1、先利用itertools生成所有24中4个数字的全排列。
2、然后根据时间格式来判断哪些排列是有效的。
    * 小时高位是2，小时低位就是[0-3]
    * 小时高位是[0-1]，小时低位是[0-9]
    * 分钟高位是[0-5]，分钟低位是[0-9]
3、获取所有有效时间字符串后排序，拿到最后一个就是最大的时间。
"""
