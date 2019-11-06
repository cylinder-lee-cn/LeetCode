"""
1046. 最后一块石头的重量

有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出两块最重的石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。

 

提示：

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort(reverse=True)
        while len(stones) > 1:
            y = stones[0]
            x = stones[1]
            if x == y:
                stones.pop(0)
                stones.pop(0)
            else:
                stones.pop(0)
                stones[0] = y - x
                stones.sort(reverse=True)

        return stones[0] if len(stones) == 1 else 0


s = Solution()
print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))


"""
此题解法：
* python默认只有最小堆，没有最大堆。如果有最大堆，可以直接使用最大堆
* 使用list，从大到小排序
* 前两个比较，如果不相同，就在pop掉第一个，在第二个位置修改成y-x（再排序一次），否则前两个都pop掉
* 最后看数组中剩余1个还是没有
"""