"""
997. 找到小镇的法官

在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。

如果小镇的法官真的存在，那么：

小镇的法官不相信任何人。
每个人（除了小镇法官外）都信任小镇的法官。
只有一个人同时满足属性 1 和属性 2 。
给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。

如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。

示例 1：
输入：N = 2, trust = [[1,2]]
输出：2

示例 2：
输入：N = 3, trust = [[1,3],[2,3]]
输出：3

示例 3：
输入：N = 3, trust = [[1,3],[2,3],[3,1]]
输出：-1

示例 4：
输入：N = 3, trust = [[1,2],[2,3]]
输出：-1

示例 5：
输入：N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
输出：3

提示：
1 <= N <= 1000
trust.length <= 10000
trust[i] 是完全不同的
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
"""


class Solution:
    # def findJudge(self, N: int, trust: List[List[int]]) -> int:
    def findJudge(self, N, trust):
        trelation = [[0, 0] for _ in range(N + 1)]
        for a, b in trust:
            trelation[b][1] = trelation[b][1] + 1
            trelation[a][0] = trelation[a][0] + 1
        # print(trelation)

        for i in range(1, N + 1):
            if trelation[i][0] == 0 and trelation[i][1] == N - 1:
                return i
        return -1


s = Solution()
print(s.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
print(s.findJudge(3, [[1, 2], [2, 3]]))
print(s.findJudge(3, [[1, 3], [2, 3], [3, 1]]))
print(s.findJudge(3, [[1, 3], [2, 3]]))
print(s.findJudge(2, [[1, 2]]))
print(s.findJudge(1, []))
"""
此题解法：
* 按照提示中，是不会出现自己信任自己的情况
* 构造一个多维数组，[0，0]x N，数组的索引对应第几位人，左边表示自己信任的，右边表示信任自己的
* 遍历trust，依次填充这个多维数组
* 再遍历这个数组，如果其中一个左边是0，右边是N-1，那么就是法官
"""
