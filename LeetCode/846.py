"""
846. 一手顺子

爱丽丝有一手（hand）由整数数组给定的牌。
现在她想把牌重新排列成组，使得每个组的大小都是 W，且由 W 张连续的牌组成。
如果她可以完成分组就返回 true，否则返回 false。

示例 1：
输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
输出：true
解释：爱丽丝的手牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。

示例 2：
输入：hand = [1,2,3,4,5], W = 4
输出：false
解释：爱丽丝的手牌无法被重新排列成几个大小为 4 的组。

提示：
1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""


class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        import collections

        hdict = collections.Counter(hand)
        hd_len = len(hdict)
        hand_len = len(hand)

        if (hand_len % W > 0):
            return False
        if (W == 1):
            return True
        if (W == hand_len and hand_len != hd_len):
            return False

        groups = hand_len // W
        g = 0

        for x in sorted(hdict.keys()):
            t = hdict[x]
            if t > 0:
                for i in range(W):
                    hdict[x + i] = hdict[x + i] - t
                    if hdict[x + i] < 0:
                        return False
                g = g + t
            if g > groups:
                break
        # return all(n == 0 for n in hdict.values())
        return True


s = Solution()
print(s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
print(s.isNStraightHand([1, 2, 3, 4, 5], 4))
print(s.isNStraightHand([1, 1, 2, 2, 3, 3], 3))
"""
此题解法：
* 还是利用字典，用Counter将hand中的数字和出现的次数都放入字典
* 然后遍历hand，当hdict[x]数量>0时，把对应连续的W个数字的次数都减
"""
